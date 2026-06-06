"""Tests for MCP Doctor registry."""
from mcp_doctor.registry import get_registry, search_servers


def test_registry_not_empty():
    registry = get_registry()
    assert len(registry) > 10


def test_search_by_category():
    results = search_servers("database")
    assert len(results) > 0
    # search matches name, description, OR category — all results should match at least one
    for r in results:
        assert ("database" in r.get("category", "")
                or "database" in r.get("name", "").lower()
                or "database" in r.get("description", "").lower())


def test_search_by_name():
    results = search_servers("github")
    assert len(results) > 0
