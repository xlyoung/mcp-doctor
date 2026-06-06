"""Security scanner for MCP servers."""
import re
from typing import Any


def scan_server(server_ref: str) -> dict[str, Any]:
    """Scan an MCP server for security issues."""
    issues: list[dict] = []
    source = _fetch_source(server_ref)
    checks = [
        _check_prompt_injection,
        _check_path_traversal,
        _check_credential_leakage,
        _check_network_exfiltration,
        _check_ssrf,
        _check_command_injection,
        _check_unconstrained_params,
        _check_tool_access_control,
        _check_excessive_permissions,
    ]
    for check in checks:
        found = check(source, server_ref)
        issues.extend(found)

    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for issue in issues:
        sev = issue.get("severity", "low")
        if sev in counts:
            counts[sev] += 1

    return {"server": server_ref, "issues": issues, **counts}


def _fetch_source(server_ref: str) -> str:
    """Fetch server source (README) for analysis."""
    import httpx

    # npm-style refs
    if server_ref.startswith("@") or "/" not in server_ref.split("/")[-1]:
        pkg = server_ref.lstrip("@").replace("/", "%2F")
        try:
            r = httpx.get(f"https://registry.npmjs.org/{pkg}", timeout=10, follow_redirects=True)
            if r.status_code == 200:
                data = r.json()
                repo = data.get("repository", {})
                url = repo.get("url", "") if isinstance(repo, dict) else str(repo)
                m = re.search(r"github\.com[:/]([^/]+/[^/.]+)", url)
                if m:
                    return _fetch_github_readme(m.group(1))
        except Exception:
            pass

    # Direct GitHub ref
    if "/" in server_ref and not server_ref.startswith(("/", ".")):
        return _fetch_github_readme(server_ref)
    return ""


def _fetch_github_readme(repo: str) -> str:
    """Fetch README from GitHub."""
    import httpx
    for branch in ("main", "master"):
        try:
            r = httpx.get(
                f"https://raw.githubusercontent.com/{repo}/{branch}/README.md",
                timeout=10, follow_redirects=True,
            )
            if r.status_code == 200:
                return r.text
        except Exception:
            pass
    return ""


def _check_prompt_injection(source: str, server: str) -> list[dict]:
    """Check for prompt injection vectors."""
    issues = []
    patterns = [
        (r"system\s*prompt.*\+.*input", "User input concatenated into system prompt"),
        (r"eval\(.*request", "Evaluating request data directly"),
    ]
    for pat, desc in patterns:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({"severity": "high", "title": "Potential prompt injection", "detail": desc})
    return issues


def _check_path_traversal(source: str, server: str) -> list[dict]:
    """Check for path traversal vulnerabilities."""
    issues = []
    if re.search(r"open\(.*\+.*request", source, re.IGNORECASE):
        issues.append({
            "severity": "critical",
            "title": "Path traversal risk",
            "detail": "File path constructed from user input without sanitization",
        })
    return issues


def _check_credential_leakage(source: str, server: str) -> list[dict]:
    """Check for credential exposure risks."""
    issues = []
    cred_pattern = r'(api[_-]?key|secret|token|password)\s*=\s*["\'][^"\']{8,}'
    if re.search(cred_pattern, source, re.IGNORECASE):
        issues.append({
            "severity": "high",
            "title": "Hardcoded credential detected",
            "detail": "Possible API key or secret embedded in source",
        })
    return issues


def _check_network_exfiltration(source: str, server: str) -> list[dict]:
    """Check for data exfiltration patterns."""
    issues = []
    suspicious = [
        (r"webhook\.site", "External webhook endpoint (possible data exfiltration)"),
        (r"ngrok\.io", "Tunnel endpoint exposed"),
    ]
    for pat, desc in suspicious:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({"severity": "critical", "title": "Network exfiltration risk", "detail": desc})
    return issues


def _check_ssrf(source: str, server: str) -> list[dict]:
    """Check for Server-Side Request Forgery vulnerabilities."""
    issues = []
    ssrf_patterns = [
        (r"requests\.(get|post|put)\(.*f['\"]http", "Dynamic URL construction from user input (requests)"),
        (r"httpx\.(get|post|put)\(.*f['\"]http", "Dynamic URL construction from user input (httpx)"),
        (r"fetch\(.*\+.*request", "User-controlled URL passed to fetch"),
        (r"169\.254\.169\.254", "Cloud metadata endpoint referenced (potential SSRF target)"),
        (r"localhost:\d+", "Localhost reference detected (potential SSRF to internal services)"),
    ]
    for pat, desc in ssrf_patterns:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({"severity": "high", "title": "SSRF risk", "detail": desc})
    return issues


def _check_command_injection(source: str, server: str) -> list[dict]:
    """Check for command injection vulnerabilities."""
    issues = []
    cmd_patterns = [
        (r"os\.system\(.*(?:request|input|user|args)", "User input passed to os.system()", "critical"),
        (r"subprocess\.(call|run|Popen|check_output)\(.*(?:request|input|user|args)", "User input passed to subprocess without sanitization", "critical"),
        (r"subprocess\.(call|run|Popen)\(.*shell\s*=\s*True.*request", "Shell command execution with user input", "critical"),
        (r"exec\(.*(?:request|input|user|args)", "User input passed to exec()", "critical"),
        (r"eval\((?!['\"])(?:.*(?:request|input|user|args))", "User input evaluated as code via eval()", "critical"),
        (r"child_process\.exec\(.*request", "Node.js child_process.exec with user input", "critical"),
        (r"shell\s*=\s*True", "subprocess called with shell=True (shell injection risk)", "high"),
    ]
    for pat, desc, severity in cmd_patterns:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({"severity": severity, "title": "Command injection risk", "detail": desc})
    return issues


def _check_unconstrained_params(source: str, server: str) -> list[dict]:
    """Check for unconstrained string parameters in tool definitions.

    Detects MCP tool schemas where string parameters lack maxLength, pattern,
    or enum constraints — a systematic security gap identified by the MCP
    community (see modelcontextprotocol/servers#3537). Unconstrained params
    enable DoS, prompt injection amplification, and injection chains.
    """
    issues = []
    # Look for tool parameter definitions without constraints
    param_blocks = re.finditer(
        r'"type"\s*:\s*"string".*?(?:"maxLength"|"pattern"|"enum"|"minimum"|"maximum"|})',
        source, re.DOTALL,
    )
    unconstrained = 0
    for match in param_blocks:
        block = match.group(0)
        if not re.search(r'"maxLength"|"pattern"|"enum"', block):
            unconstrained += 1

    if unconstrained >= 3:
        issues.append({
            "severity": "medium",
            "title": "Unconstrained string parameters",
            "detail": (
                f"Found {unconstrained} string parameters without maxLength/pattern/enum "
                "constraints. This enables DoS via oversized inputs and weakens the "
                "defense against prompt injection attacks."
            ),
        })

    # Also check for very long default maxLength values
    long_limits = re.finditer(r'"maxLength"\s*:\s*(\d+)', source)
    for match in long_limits:
        limit = int(match.group(1))
        if limit > 100000:
            issues.append({
                "severity": "low",
                "title": "Excessive maxLength on parameter",
                "detail": f"maxLength of {limit} chars is effectively unconstrained; consider tightening to ≤10000",
            })
    return issues


def _check_tool_access_control(source: str, server: str) -> list[dict]:
    """Check for presentation-layer-only access control.

    Detects patterns where tool access controls are enforced at discovery
    (tools/list) but not at execution (tools/call) — a bypass pattern seen
    in mcp-server-kubernetes (CVE-2026-46519).
    """
    issues = []
    has_list_filter = bool(re.search(
        r'(ALLOWED_TOOLS|ALLOW_ONLY|tools/list|ListToolsRequest).*?(filter|restrict|allow)',
        source, re.IGNORECASE | re.DOTALL,
    ))
    has_call_filter = bool(re.search(
        r'(tools/call|CallToolRequest).*?(filter|restrict|allow|check)',
        source, re.IGNORECASE | re.DOTALL,
    ))

    if has_list_filter and not has_call_filter:
        issues.append({
            "severity": "high",
            "title": "Tool access control bypass risk",
            "detail": (
                "Tool restrictions appear enforced at discovery (tools/list) but not at "
                "execution (tools/call). Clients can invoke restricted tools directly. "
                "See CVE-2026-46519 for a real-world example."
            ),
        })
    return issues


def _check_excessive_permissions(source: str, server: str) -> list[dict]:
    """Check for tools requesting broader access than needed."""
    issues = []
    danger_patterns = [
        (r'--allow[=-]all|--no-auth|--skip-auth|--disable-auth',
         "Authentication bypass flag detected"),
        (r'readFile.*\*|writeFile.*\*|readdirSync.*\/$',
         "Unrestricted filesystem glob (reads/writes everything)"),
        (r"chmod\s+[0-7]*7[0-7]*\s",
         "Setting world-readable/writable permissions"),
    ]
    for pat, desc in danger_patterns:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({
                "severity": "medium",
                "title": "Excessive permissions",
                "detail": desc,
            })
    return issues
