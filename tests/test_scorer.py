"""Tests for MCP Doctor scorer."""
from mcp_doctor.scorer import score_server


def test_score_returns_dict():
    result = score_server("modelcontextprotocol/servers")
    assert isinstance(result, dict)
    assert "total" in result
    assert 0 <= result["total"] <= 100


def test_score_categories():
    result = score_server("modelcontextprotocol/servers")
    assert "Security" in result["categories"]
    assert "Maintenance" in result["categories"]
