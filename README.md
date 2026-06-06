# 🩺 MCP Doctor

**Scan · Score · Install — Your MCP Server Toolkit**

[![GitHub Stars](https://img.shields.io/github/stars/xlyoung/mcp-doctor?style=social)](https://github.com/xlyoung/mcp-doctor)
[![PyPI](https://img.shields.io/pypi/v/mcp-doctor.svg)](https://pypi.org/project/mcp-doctor/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> The missing security and quality toolkit for the [Model Context Protocol](https://modelcontextprotocol.io/) ecosystem.
> Scan MCP servers for vulnerabilities, score their quality, compare alternatives, and install with confidence.

---

## 🤔 Why MCP Doctor?

The MCP ecosystem is exploding — hundreds of servers, but no way to know which ones are safe, well-maintained, or even work. MCP Doctor is your one-stop CLI to navigate the MCP jungle.

**Before installing an MCP server, run it through the Doctor.**

## ✨ Features

- 🔒 **Security Scan** — Detect prompt injection vectors, unsafe file access, network exfiltration risks, and credential leakage
- 📊 **Quality Score** — Automated 0-100 scoring based on: security, maintenance, documentation, testing, community
- ⚖️ **Compare** — Side-by-side comparison of two MCP servers across all quality dimensions
- 📦 **Registry** — Curated database of 50+ popular MCP servers with pre-computed scores and categories
- ⚡ **Quick Install** — `mcp-doctor install <server>` — one command to scan + score + install
- 📈 **Stats** — Registry overview with category breakdowns and averages

## 🚀 Quick Start

```bash
# Install
pip install mcp-doctor

# Scan an MCP server for security issues
mcp-doctor scan @modelcontextprotocol/server-filesystem

# Score a server's quality (0-100)
mcp-doctor score modelcontextprotocol/servers

# Compare two servers side-by-side
mcp-doctor compare @modelcontextprotocol/server-postgres mcp-server-mysql

# See top-rated servers by category
mcp-doctor list --category database --sort score

# Install with confidence (blocks on critical security issues)
mcp-doctor install @modelcontextprotocol/server-github

# View registry stats
mcp-doctor stats
```

## 📊 Quality Score Breakdown

Each MCP server receives a score from 0-100:

| Category | Weight | What it checks |
|----------|--------|----------------|
| Security | 35% | Prompt injection, path traversal, network safety |
| Maintenance | 25% | Commit frequency, issue response time, release cadence |
| Documentation | 15% | README quality, API docs, examples |
| Testing | 15% | Test coverage, CI status, integration tests |
| Community | 10% | Stars, contributors, ecosystem integrations |

## 🔒 Security Checks

MCP Doctor scans for common MCP vulnerability patterns:

- **Prompt Injection** — User input flowing directly into LLM prompts without sanitization
- **Path Traversal** — File system tools accepting `../` in paths without validation
- **Credential Leakage** — API keys, tokens, or secrets exposed in logs or responses
- **Network Exfiltration** — Suspicious external endpoints (webhook.site, ngrok tunnels)
- **Supply Chain** — Typosquatting, abandoned dependencies, known CVEs

## ⚖️ Compare Servers

Can't decide between two MCP servers? Compare them:

```bash
$ mcp-doctor compare @modelcontextprotocol/server-postgres mcp-server-mysql

           MCP Server Comparison
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Metric           ┃ postgres  ┃ mysql     ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Overall Score    │   90/100  │   78/100  │
│ Security         │    90     │    80     │
│ Maintenance      │    95     │    60     │
│ Documentation    │    70     │    50     │
│ Testing          │    55     │    50     │
│ Community        │    95     │    80     │
│ Security Issues  │    0      │    0      │
└──────────────────┴───────────┴───────────┘

✔ Recommendation: @modelcontextprotocol/server-postgres (score 90 vs 78)
```

## 📖 MCP Server Registry

Browse the full registry: **[REGISTRY.md](./REGISTRY.md)**

Categories:
- 🗄️ Database — PostgreSQL, MySQL, SQLite, Redis, MongoDB, Qdrant, ClickHouse, Supabase, Neon
- 📁 File System — Local files, S3
- 🌐 Web — Brave Search, Playwright, Puppeteer, Firecrawl, Chrome MCP
- 🔧 DevOps — GitHub (official), GitLab, Docker, Kubernetes, Git
- 💬 Communication — Slack, Discord, Gmail, Telegram
- 🧠 Knowledge — Notion, Obsidian, Memory, Confluence
- 🤖 AI/ML — FastMCP, Hugging Face, Replicate, Ollama
- 🔒 Security — Semgrep, NVD CVE lookup
- 🎨 Design — Figma Context MCP
- 📋 Productivity — Google Maps, Linear, Airtable, Google Calendar, Todoist

## 🛠️ Development

```bash
git clone https://github.com/xlyoung/mcp-doctor.git
cd mcp-doctor
pip install -e ".[dev]"
pytest
```

## 📝 Contributing

Found an MCP server that should be in the registry? Open an [issue](https://github.com/xlyoung/mcp-doctor/issues/new) or submit a PR!

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📄 License

MIT — do whatever you want with it.

---

*Built for the MCP community. Star ⭐ if you find it useful!*
