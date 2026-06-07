"""Tests for MCP Doctor scanner."""
from mcp_doctor.scanner import scan_server


def test_scan_returns_dict():
    result = scan_server("nonexistent/server-xyz")
    assert isinstance(result, dict)
    assert "issues" in result
    assert "critical" in result


def test_scan_known_server():
    """Scan a well-known server — should return with minimal critical issues."""
    result = scan_server("modelcontextprotocol/servers")
    assert isinstance(result, dict)
    # When network is available, check critical count; when unavailable, just check structure
    if result.get("issues") is not None:
        assert result["critical"] <= 1  # Known good repo
    assert "server" in result
