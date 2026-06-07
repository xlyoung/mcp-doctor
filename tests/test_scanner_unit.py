"""Tests for MCP Doctor scanner — unit tests (no network)."""
from mcp_doctor.scanner import (
    _check_prompt_injection,
    _check_path_traversal,
    _check_credential_leakage,
    _check_network_exfiltration,
    _check_ssrf,
    _check_command_injection,
    _check_unconstrained_params,
    _check_tool_access_control,
    _check_excessive_permissions,
)


# ── Prompt Injection ────────────────────────────────────────────────

def test_prompt_injection_detects_system_prompt_concat():
    source = 'system prompt = "Base" + user_input'
    issues = _check_prompt_injection(source, "test")
    assert any("prompt injection" in i["title"].lower() for i in issues)


def test_prompt_injection_clean():
    source = 'def handle(request): return sanitize(request.text)'
    issues = _check_prompt_injection(source, "test")
    assert len(issues) == 0


# ── Path Traversal ──────────────────────────────────────────────────

def test_path_traversal_detects_open_plus_request():
    source = 'open("/data/" + request.filename, "r")'
    issues = _check_path_traversal(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "critical"


def test_path_traversal_clean():
    source = 'open("/etc/config.yaml", "r")'
    issues = _check_path_traversal(source, "test")
    assert len(issues) == 0


# ── Credential Leakage ─────────────────────────────────────────────

def test_credential_leakage_detects_api_key():
    source = 'api_key = "sk-1234567890abcdef1234567890"'
    issues = _check_credential_leakage(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "high"


def test_credential_leakage_clean():
    source = 'api_key = os.environ["API_KEY"]'
    issues = _check_credential_leakage(source, "test")
    assert len(issues) == 0


# ── Network Exfiltration ────────────────────────────────────────────

def test_exfiltration_detects_webhook_site():
    source = 'url = "https://webhook.site/abc123"'
    issues = _check_network_exfiltration(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "critical"


def test_exfiltration_detects_ngrok():
    source = 'endpoint = "https://abc.ngrok.io/hook"'
    issues = _check_network_exfiltration(source, "test")
    assert len(issues) == 1


def test_exfiltration_clean():
    source = 'url = "https://api.example.com/v1"'
    issues = _check_network_exfiltration(source, "test")
    assert len(issues) == 0


# ── SSRF ────────────────────────────────────────────────────────────

def test_ssrf_detects_cloud_metadata():
    source = 'r = requests.get("http://169.254.169.254/latest/meta-data/")'
    issues = _check_ssrf(source, "test")
    assert any("metadata" in i["detail"].lower() for i in issues)


def test_ssrf_detects_localhost():
    source = 'fetch("http://localhost:8080/admin")'
    issues = _check_ssrf(source, "test")
    assert any("localhost" in i["detail"].lower() for i in issues)


def test_ssrf_clean():
    source = 'r = requests.get("https://api.github.com/repos")'
    issues = _check_ssrf(source, "test")
    assert len(issues) == 0


# ── Command Injection ──────────────────────────────────────────────

def test_command_injection_detects_os_system():
    source = 'os.system("ls " + request.args["dir"])'
    issues = _check_command_injection(source, "test")
    assert len(issues) >= 1
    assert issues[0]["severity"] == "critical"


def test_command_injection_detects_shell_true():
    source = 'subprocess.run(cmd, shell=True)'
    issues = _check_command_injection(source, "test")
    assert any(i["severity"] == "high" for i in issues)


def test_command_injection_clean():
    source = 'subprocess.run(["ls", "-la"], capture_output=True)'
    issues = _check_command_injection(source, "test")
    assert len(issues) == 0


# ── Excessive Permissions ──────────────────────────────────────────

def test_excessive_permissions_detects_allow_all():
    source = 'mcp-server --allow-all --port 3000'
    issues = _check_excessive_permissions(source, "test")
    assert len(issues) >= 1
    assert "auth" in issues[0]["detail"].lower()


def test_excessive_permissions_detects_chmod():
    source = 'chmod 777 /tmp/data'
    issues = _check_excessive_permissions(source, "test")
    assert len(issues) >= 1


def test_excessive_permissions_clean():
    source = 'server.listen(3000)'
    issues = _check_excessive_permissions(source, "test")
    assert len(issues) == 0


# ── Unconstrained Parameters ──────────────────────────────────────

def test_unconstrained_params_detects_many_strings():
    source = '''
    {"type": "object", "properties": {
        "a": {"type": "string"},
        "b": {"type": "string"},
        "c": {"type": "string"},
        "d": {"type": "string"}
    }}
    '''
    issues = _check_unconstrained_params(source, "test")
    assert len(issues) >= 1


def test_unconstrained_params_clean_with_maxlength():
    source = '''
    {"type": "object", "properties": {
        "name": {"type": "string", "maxLength": 100},
        "query": {"type": "string", "maxLength": 500, "pattern": "[a-z]+"}
    }}
    '''
    issues = _check_unconstrained_params(source, "test")
    # Should not flag — has maxLength/pattern
    assert len([i for i in issues if "unconstrained" in i["title"].lower()]) == 0


# ── Tool Access Control ────────────────────────────────────────────

def test_tool_access_control_detects_list_only_filter():
    source = '''
    ALLOWED_TOOLS = ["search", "read"]
    def handle_list(request: ListToolsRequest):
        return filter(allowed, tools)
    def handle_call(request: CallToolRequest):
        return execute(request.tool)
    '''
    issues = _check_tool_access_control(source, "test")
    assert len(issues) == 1
    assert "bypass" in issues[0]["title"].lower()


def test_tool_access_control_clean_with_both_filters():
    source = '''
    ALLOWED_TOOLS = ["search"]
    def handle_list(request: ListToolsRequest):
        return filter(allowed, tools)
    def handle_call(request: CallToolRequest):
        check_allowed(request.tool)
        return execute(request.tool)
    '''
    issues = _check_tool_access_control(source, "test")
    assert len(issues) == 0
