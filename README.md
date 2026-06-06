# 🩺 MCP Doctor

**Scan · Score · Install — Your MCP Server Toolkit**

[![GitHub Stars](https://img.shields.io/github/stars/xlyoung/mcp-doctor?style=social)](https://github.com/xlyoung/mcp-doctor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> The missing toolkit for the [Model Context Protocol](https://modelcontextprotocol.io/) ecosystem.
> Scan MCP servers for security issues, score their quality, and install with confidence.

---

## 🤔 Why MCP Doctor?

The MCP ecosystem is exploding — hundreds of servers, but no way to know which ones are safe, well-maintained, or even work. MCP Doctor is your one-stop CLI to navigate the MCP jungle.

**Before installing an MCP server, run it through the Doctor.**

## ✨ Features

- 🔒 **Security Scan** — Detect prompt injection vectors, unsafe file access, network exfiltration risks, and dependency vulnerabilities
- 📊 **Quality Score** — Automated scoring based on: code quality, test coverage, documentation, maintenance activity, community health
- 📦 **Registry** — Curated database of 200+ MCP servers with pre-computed scores and categories
- ⚡ **Quick Install** — `mcp-doctor install <server>` — one command to scan + install + configure
- 🔄 **Auto-Update** — Tracks upstream changes and alerts on breaking updates or security patches

## 🚀 Quick Start

```bash
# Install
pip install mcp-doctor

# Scan an MCP server before installing
mcp-doctor scan @modelcontextprotocol/server-filesystem

# See top-rated MCP servers by category
mcp-doctor list --category database --sort score

# Install with confidence
mcp-doctor install @modelcontextprotocol/server-github
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
- **Excessive Permissions** — Tools requesting broader access than their stated purpose
- **Supply Chain** — Typosquatting, abandoned dependencies, known CVEs

## 📖 MCP Server Registry

Browse the full registry: [REGISTRY.md](./REGISTRY.md)

Categories:
- 🗄️ Database — PostgreSQL, MySQL, Redis, MongoDB, Qdrant
- 📁 File System — Local files, S3, Google Drive, Dropbox
- 🌐 Web — Search, scraping, browser automation
- 🔧 DevOps — GitHub, GitLab, Docker, Kubernetes
- 💬 Communication — Slack, Discord, Email, Telegram
- 🧠 Knowledge — Notion, Obsidian, Confluence
- 🤖 AI/ML — Hugging Face, Replicate, Ollama

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
