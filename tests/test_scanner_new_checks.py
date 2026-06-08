"""Tests for MCP Doctor scanner — new security checks (no network)."""
from mcp_doctor.scanner import (
    _check_unsafe_deserialization,
    _check_dynamic_import,
    _check_log_injection,
)


# ── Unsafe Deserialization ─────────────────────────────────────────

def test_deserialization_detects_pickle_load():
    source = 'data = pickle.loads(request.body)'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "critical"
    assert "pickle" in issues[0]["detail"].lower()


def test_deserialization_detects_pickle_load_file():
    source = 'obj = pickle.load(open("data.pkl", "rb"))'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1


def test_deserialization_detects_yaml_load_unsafe():
    source = 'config = yaml.load(user_input)'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "high"


def test_deserialization_clean_yaml_safe_load():
    source = 'config = yaml.safe_load(file_content)'
    issues = _check_unsafe_deserialization(source, "test")
    # safe_load should not be flagged (the regex excludes SafeLoader)
    assert len([i for i in issues if "yaml" in i["detail"].lower()]) == 0


def test_deserialization_detects_marshal():
    source = 'code = marshal.loads(raw_bytes)'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "critical"


def test_deserialization_detects_jsonpickle():
    source = 'obj = jsonpickle.decode(json_str)'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "critical"


def test_deserialization_detects_shelve():
    source = 'db = shelve.open("user_data")'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "high"


def test_deserialization_clean():
    source = 'data = json.loads(response.text)'
    issues = _check_unsafe_deserialization(source, "test")
    assert len(issues) == 0


# ── Dynamic Import ─────────────────────────────────────────────────

def test_dynamic_import_detects_import_with_request():
    source = 'mod = __import__(request.args["module"])'
    issues = _check_dynamic_import(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "high"


def test_dynamic_import_detects_importlib_with_input():
    source = 'mod = importlib.import_module(user_input)'
    issues = _check_dynamic_import(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "high"


def test_dynamic_import_detects_require_with_request():
    source = 'const lib = require(request.body.module)'
    issues = _check_dynamic_import(source, "test")
    assert len(issues) == 1


def test_dynamic_import_clean():
    source = 'import json\nimport os'
    issues = _check_dynamic_import(source, "test")
    assert len(issues) == 0


# ── Log Injection ──────────────────────────────────────────────────

def test_log_injection_detects_concat():
    source = 'logging.info("User logged in: " + request.user)'
    issues = _check_log_injection(source, "test")
    assert len(issues) == 1
    assert issues[0]["severity"] == "low"


def test_log_injection_detects_fstring():
    source = 'logger.error(f"Failed login for {request.args[\"user\"]}")'
    issues = _check_log_injection(source, "test")
    assert len(issues) == 1


def test_log_injection_clean():
    source = 'logging.info("Server started on port 8080")'
    issues = _check_log_injection(source, "test")
    assert len(issues) == 0
