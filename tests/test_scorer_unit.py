"""Tests for MCP Doctor scorer — unit tests (no network)."""
from datetime import datetime, timezone, timedelta
from mcp_doctor.scorer import (
    _score_security,
    _score_maintenance,
    _score_docs,
    _score_testing,
    _score_community,
)


# ── Security Scoring ────────────────────────────────────────────────

def test_security_base_score():
    gh = {}
    assert _score_security(gh) == 80


def test_security_with_policy():
    gh = {"has_security_policy": True}
    assert _score_security(gh) == 90


def test_security_private_repo():
    gh = {"private": True}
    assert _score_security(gh) == 50


def test_security_max_score():
    gh = {"has_security_policy": True, "private": False}
    assert _score_security(gh) == 90


# ── Maintenance Scoring ─────────────────────────────────────────────

def test_maintenance_recent_push():
    recent = (datetime.now(timezone.utc) - timedelta(days=3)).isoformat()
    gh = {"pushed_at": recent}
    score = _score_maintenance(gh)
    assert score >= 90


def test_maintenance_stale_repo():
    stale = (datetime.now(timezone.utc) - timedelta(days=400)).isoformat()
    gh = {"pushed_at": stale}
    score = _score_maintenance(gh)
    assert score <= 30


def test_maintenance_many_open_issues():
    recent = (datetime.now(timezone.utc) - timedelta(days=3)).isoformat()
    gh = {"pushed_at": recent, "open_issues_count": 200}
    score = _score_maintenance(gh)
    # Should be penalized for many open issues
    assert score <= 90


def test_maintenance_no_data():
    gh = {}
    score = _score_maintenance(gh)
    assert 0 <= score <= 100


# ── Documentation Scoring ──────────────────────────────────────────

def test_docs_base_score():
    gh = {}
    assert _score_docs(gh) == 50


def test_docs_full_score():
    gh = {"has_pages": True, "description": "A great server", "homepage": "https://example.com"}
    assert _score_docs(gh) == 90


# ── Testing Scoring ────────────────────────────────────────────────

def test_testing_base_score():
    gh = {}
    assert _score_testing(gh) == 50


def test_testing_with_wiki():
    gh = {"has_wiki": True}
    assert _score_testing(gh) == 55


# ── Community Scoring ──────────────────────────────────────────────

def test_community_popular():
    gh = {"stargazers_count": 15000, "forks_count": 5000}
    score = _score_community(gh)
    assert score >= 90


def test_community_small():
    gh = {"stargazers_count": 5, "forks_count": 1}
    score = _score_community(gh)
    assert score <= 40


def test_community_no_stars():
    gh = {"stargazers_count": 0, "forks_count": 0}
    score = _score_community(gh)
    assert score == 30


def test_community_high_fork_ratio():
    gh = {"stargazers_count": 100, "forks_count": 50}
    score = _score_community(gh)
    # High fork ratio bonus
    assert score >= 60
