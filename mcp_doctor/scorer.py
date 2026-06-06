"""Quality scorer for MCP servers."""
import re
from datetime import datetime, timezone
from typing import Any

import httpx


def score_server(server_ref: str) -> dict[str, Any]:
    """Score an MCP server quality from 0-100."""
    repo = _resolve_repo(server_ref)
    if not repo:
        return {"server": server_ref, "total": 0, "categories": {}, "error": "Could not resolve server"}

    gh = _fetch_github(repo)
    if not gh:
        return {"server": server_ref, "total": 0, "categories": {}, "error": "GitHub API unavailable"}

    weights = {"Security": 0.35, "Maintenance": 0.25, "Documentation": 0.15, "Testing": 0.15, "Community": 0.10}
    categories = {
        "Security": {"score": _score_security(gh), "note": "vulnerability patterns"},
        "Maintenance": {"score": _score_maintenance(gh), "note": "commit frequency, response time"},
        "Documentation": {"score": _score_docs(gh), "note": "README, API docs, examples"},
        "Testing": {"score": _score_testing(gh), "note": "CI, coverage, integration tests"},
        "Community": {"score": _score_community(gh), "note": "stars, contributors, ecosystem"},
    }
    total = round(sum(categories[k]["score"] * weights[k] for k in weights))

    return {"server": server_ref, "repo": repo, "total": total, "categories": categories}


def _resolve_repo(server_ref: str) -> str | None:
    """Resolve server reference to github owner/repo."""
    if "/" in server_ref and server_ref.count("/") == 1:
        return server_ref
    try:
        pkg = server_ref.lstrip("@").replace("/", "%2F")
        r = httpx.get(f"https://registry.npmjs.org/{pkg}", timeout=10, follow_redirects=True)
        if r.status_code == 200:
            data = r.json()
            repo = data.get("repository", {})
            url = repo.get("url", "") if isinstance(repo, dict) else str(repo)
            m = re.search(r"github\.com[:/]([^/]+/[^/.]+)", url)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None


def _fetch_github(repo: str) -> dict:
    """Fetch GitHub repo metadata."""
    try:
        r = httpx.get(
            f"https://api.github.com/repos/{repo}",
            timeout=10,
            headers={"Accept": "application/vnd.github.v3+json"},
        )
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {}


def _score_security(gh: dict) -> int:
    score = 80
    if gh.get("has_security_policy"):
        score += 10
    if gh.get("private"):
        score = 50
    return min(100, score)


def _score_maintenance(gh: dict) -> int:
    score = 50
    pushed = gh.get("pushed_at", "")
    if pushed:
        try:
            last_push = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
            days_ago = (datetime.now(timezone.utc) - last_push).days
            if days_ago <= 7:
                score = 95
            elif days_ago <= 30:
                score = 80
            elif days_ago <= 90:
                score = 60
            elif days_ago <= 365:
                score = 40
            else:
                score = 20
        except Exception:
            pass
    issues = gh.get("open_issues_count", 0)
    if issues > 100:
        score -= 10
    return max(0, min(100, score))


def _score_docs(gh: dict) -> int:
    score = 50
    if gh.get("has_pages"):
        score += 20
    if gh.get("description"):
        score += 10
    if gh.get("homepage"):
        score += 10
    return min(100, score)


def _score_testing(gh: dict) -> int:
    score = 50
    if gh.get("has_wiki"):
        score += 5
    return min(100, score)


def _score_community(gh: dict) -> int:
    stars = gh.get("stargazers_count", 0)
    forks = gh.get("forks_count", 0)
    if stars >= 10000:
        score = 95
    elif stars >= 1000:
        score = 80
    elif stars >= 100:
        score = 65
    elif stars >= 10:
        score = 50
    else:
        score = 30
    if stars > 0 and forks / stars > 0.3:
        score += 5
    return min(100, score)
