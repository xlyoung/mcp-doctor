# 🩺 MCP Doctor

**Scan · Score · Install — Your MCP Server Toolkit**

[![GitHub Stars](https://img.shields.io/github/stars/xlyoung/mcp-doctor?style=social)](https://github.com/xlyoung/mcp-doctor)
[![CI](https://github.com/xlyoung/mcp-doctor/actions/workflows/ci.yml/badge.svg)](https://github.com/xlyoung/mcp-doctor/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mcpdoctor.svg)](https://pypi.org/project/mcpdoctor/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mcpdoctor.svg)](https://pypi.org/project/mcpdoctor/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Security Scanner](https://img.shields.io/badge/security-scanner-red.svg)](https://github.com/xlyoung/mcp-doctor#-security-checks)
[![MCP Compatible](https://img.shields.io/badge/MCP-compatible-brightgreen.svg)](https://modelcontextprotocol.io/)

> The missing security and quality toolkit for the [Model Context Protocol](https://modelcontextprotocol.io/) ecosystem.
> Scan MCP servers for vulnerabilities, score their quality, compare alternatives, and install with confidence.

---

## 🤔 Why MCP Doctor?

The MCP ecosystem is exploding — hundreds of servers, but no way to know which ones are safe, well-maintained, or even work. MCP Doctor is your one-stop CLI to navigate the MCP jungle.

**Before installing an MCP server, run it through the Doctor.**

### MCP Doctor vs Other Tools

| Feature | MCP Doctor | mcp-audit | mcpaudit | MCPSec |
|---------|-----------|-----------|----------|--------|
| Security scanning | ✅ | ✅ | ✅ | ✅ |
| Quality scoring (0-100) | ✅ | ❌ | ❌ | ❌ |
| Server comparison | ✅ | ❌ | ❌ | ❌ |
| Curated registry (95+) | ✅ | ❌ | ❌ | ❌ |
| One-command install | ✅ | ❌ | ❌ | ❌ |
| Categories & browsing | ✅ | ❌ | ❌ | ❌ |
| CI/CD integration | ✅ | ✅ | ❌ | ✅ |
| CI/CD audit (exit codes) | ✅ | ❌ | ❌ | ❌ |

MCP Doctor is the only tool that combines **security scanning**, **quality scoring**, **server comparison**, and a **curated registry** into a single CLI.

## ✨ Features

- 🔒 **Security Scan** — 8 detection engines: prompt injection, path traversal, credential leakage, network exfiltration, command injection, SSRF, supply chain, and excessive permissions
- 📊 **Quality Score** — Automated 0-100 scoring based on: security, maintenance, documentation, testing, community
- ⚖️ **Compare** — Side-by-side comparison of two MCP servers across all quality dimensions
- 📦 **Registry** — Curated database of 100+ popular MCP servers with pre-computed scores and categories
- ⚡ **Quick Install** — `mcp-doctor install <server>` — one command to scan + score + install
- 🩺 **CI/CD Audit** — `mcp-doctor audit <server>` — full report with exit codes for pipelines
- 📈 **Stats** — Registry overview with category breakdowns and averages

## 🚀 Quick Start

```bash
# Install
pip install mcpdoctor

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

# Full audit for CI/CD (exits non-zero on failure)
mcp-doctor audit @modelcontextprotocol/server-filesystem --threshold 60
mcp-doctor audit @modelcontextprotocol/server-filesystem --json  # machine-readable

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
- **SSRF** — Server-side request forgery via unvalidated URL parameters
- **Command Injection** — Shell command execution with unsanitized input
- **Excessive Permissions** — Auth bypass flags, unrestricted filesystem globs, world-readable permissions
- **Unconstrained Parameters** — String params without maxLength/pattern/enum (DoS + injection chain risk)
- **Tool Access Control Bypass** — Presentation-layer filtering without execution-layer enforcement (CVE-2026-46519 pattern)

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
- 🗄️ Database — PostgreSQL, MySQL, SQLite, Redis, MongoDB, Qdrant, ClickHouse, Supabase, Neon, Google Toolbox
- 📁 File System — Local files, S3
- 🌐 Web — Brave Search, Playwright, Puppeteer, Firecrawl, Chrome MCP, BrowserMCP, bb-browser
- 🔧 DevOps — GitHub (official & MCP), GitLab, Docker, Kubernetes, Git, XcodeBuild
- 💬 Communication — Slack, Discord, Gmail, Telegram, WhatsApp
- 🧠 Knowledge — Notion, Obsidian, Memory, Confluence
- 🤖 AI/ML — FastMCP, Hugging Face, Replicate, Ollama
- 🔒 Security — Semgrep, NVD CVE, GhidraMCP, MCP Audit, MCPSec, HexStrike AI
- 🎨 Design — Figma Context MCP
- 📋 Productivity — Google Maps, Linear, Airtable, Google Calendar, Todoist, Kreuzberg
- 🖥️ System — DesktopCommanderMCP, Windows-MCP
- 🛠️ Developer Tools — MCP Inspector, git-mcp, MCP Registry
- ☁️ Cloud — AWS (awslabs), ActivePieces
- 🏗️ Framework — mcp-use
- 🔄 Automation — ActivePieces

## 🛠️ Development

```bash
git clone https://github.com/xlyoung/mcp-doctor.git
cd mcp-doctor
pip install -e ".[dev]"
pytest
```

## 🤝 Contributing

Found an MCP server that should be in the registry? Open an [issue](https://github.com/xlyoung/mcp-doctor/issues/new) or submit a PR!

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 🔐 Security

Found a security vulnerability? See [SECURITY.md](./SECURITY.md) for responsible disclosure guidelines.

## 📜 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for release history.

## 📄 License

MIT — do whatever you want with it.

---

*Built for the MCP community. Star ⭐ if you find it useful!*
