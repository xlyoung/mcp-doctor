"""Tests for MCP Doctor registry."""
from mcp_doctor.registry import get_registry, search_servers


def test_registry_not_empty():
    registry = get_registry()
    assert len(registry) > 10


def test_search_by_category():
    results = search_servers("database")
    assert len(results) > 0
    assert all("database" in r.get("category", "") for r in results)


def test_search_by_name():
    results = search_servers("github")
    assert len(results) > 0
