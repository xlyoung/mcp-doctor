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
    assert result["critical"] <= 1  # Known good repo
