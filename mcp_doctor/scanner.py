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
        (r"os\.system\(.*request", "User input passed to os.system()"),
        (r"subprocess\.(call|run|Popen)\(.*shell\s*=\s*True.*request", "Shell command execution with user input"),
        (r"exec\(.*request", "User input passed to exec()"),
        (r"child_process\.exec\(.*request", "Node.js child_process.exec with user input"),
    ]
    for pat, desc in cmd_patterns:
        if re.search(pat, source, re.IGNORECASE):
            issues.append({"severity": "critical", "title": "Command injection risk", "detail": desc})
    return issues
