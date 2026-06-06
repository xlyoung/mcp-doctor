# Contributing to MCP Doctor

Thanks for your interest in contributing!

## How to Contribute

### Add an MCP Server to the Registry
1. Fork this repo
2. Edit `mcp_doctor/registry.py` — add your server to `_REGISTRY`
3. Include: name, repo, category, estimated stars, description, language
4. Submit a PR with title: `registry: add <server-name>`

### Report a Security Issue
Open an issue with:
- Server name and version
- Vulnerability type (prompt injection, path traversal, etc.)
- Reproduction steps

### Improve Scoring
The scorer (`mcp_doctor/scorer.py`) uses GitHub API data. If you have ideas for better heuristics, PRs welcome!

## Development Setup

```bash
git clone https://github.com/xlyoung/mcp-doctor.git
cd mcp-doctor
pip install -e ".[dev]"
pytest
```

## Code Style
- Python 3.10+ (type hints, match statements OK)
- Run `ruff check .` before submitting
- Keep functions short and focused
