# MCP Doctor Marketing Notes

## Last run: 2026-06-07 04:15 (UTC+8)

## Current Status
- Stars: 0
- Forks: 0
- Open issues: 0
- Last push: 2026-06-07
- Registry: 91+ servers (up from 85+)
- Security checks: 6 categories (added SSRF, command injection)

## Completed Actions (this run)
- [x] Added `mcp-doctor audit` command — CI/CD-friendly with exit codes, --json, --threshold
- [x] Added SSRF detection to scanner (cloud metadata, localhost, dynamic URLs)
- [x] Added command injection detection (os.system, subprocess shell=True, exec, child_process)
- [x] Added 5 new high-star servers to registry:
  - chrome-devtools-mcp (43K★) — Official Chrome DevTools
  - n8n-mcp (21K★) — Build n8n workflows
  - headroom (15K★) — Token compression
  - xiaohongshu-mcp (14K★) — China's lifestyle platform
  - fastapi-mcp (11K★) — FastAPI to MCP bridge
- [x] Updated REGISTRY.md with new top servers and category counts
- [x] Community outreach: Commented on PrefectHQ/fastmcp#4244 (audit hooks proposal, 25K★ repo)
- [x] Community outreach: Commented on AIAnytime/Awesome-MCP-Server#35 (SSRF vulnerability)
- [x] Updated README with audit command examples and CI/CD comparison row

## Previous Actions (still active)
- [x] Submitted PR/issue to punkpeye/awesome-mcp-servers (issue #7489) — waiting for merge
- [x] Submitted to mcpso (chatmcp/mcpso#1)
- [x] Added GitHub Actions CI workflow (ci.yml)
- [x] Added reusable MCP scan action (mcp-scan-action.yml)

## Registry Growth
- Started: 60 servers → 70+ → 85+ → now 91+ servers
- 20+ categories including: web, database, devops, ai, automation, framework, security, design

## Competing Tools (MCP Security Space)
- **mcp-audit** (Norbi0801) — Rust, 19 rules, AGPL-3.0, OWASP MCP Top 10
- **mcpaudit** (piiiico) — npm/npx, static scanner, multi-language
- **MCPSec** (mcp-shark) — Compliance scanner, MCP spec + OWASP
- **mcp-shield** (GaboITB) — Python, 17 detectors, Docker sandbox
- **mcpscan** (obielin) — Python, 8 rules, zero deps
- **mcp-security-scanner** (TreRB) — Node, 8 checks, static audit
- **mcp-security-scan** (agentgraph-co) — npm, static + dynamic, trust scores
- **mcp-security-auditor** (prabhubng) — npm, 7 analyzers
- **oxvault/scanner** — Go, 12/12 CVE detection, zero deps
- **jsandov/mcp-audit** — Python, 7 categories, attack graph dashboard

## MCP Doctor's Unique Position
- **Only tool** combining: security scan + quality scoring + registry + comparison + install + CI/CD audit
- Competitors focus on security scanning only
- MCP Doctor is a **complete MCP server toolkit**
- New `audit` command makes it CI/CD pipeline-ready with exit codes

## Key Directories & Listings
- [ ] punkpeye/awesome-mcp-servers — issue #7489 (pending)
- [x] chatmcp/mcpso — issue #1 comment submitted
- [ ] glama.ai/mcp/servers — not yet submitted
- [ ] Docker MCP Catalog — not yet submitted
- [ ] explainx.ai leaderboard — not yet submitted
- [ ] mcpmarket.com — not yet submitted

## Community Outreach Log
- PrefectHQ/fastmcp#4244 — Commented on audit hooks proposal (25K★ repo)
- AIAnytime/Awesome-MCP-Server#35 — Commented on SSRF vulnerability
- chatmcp/mcpso#1 — Submitted MCP Doctor entry
- punkpeye/awesome-mcp-servers#7489 — Submitted entry request (pending)

## MCP Ecosystem Context (June 2026)
- MCP has ~97M monthly SDK downloads
- ~9,400-17,000+ public MCP servers across registries
- MCP 2026-07-28 RC: stateless transport, 22 SEPs
- 30+ MCP-related CVEs filed in H1 2026
- Major adoption: Claude, ChatGPT, Gemini, VS Code, Cursor
- Enterprise readiness is top priority in 2026 roadmap

## Next Steps
1. Monitor awesome-mcp-servers issue #7489 for merge
2. Submit to glama.ai, mcpmarket.com, explainx.ai directories
3. Find 2-3 more relevant GitHub issues to recommend MCP Doctor naturally
4. Search Reddit/HN/V2EX for MCP security discussions (Strategy D)
5. Add more scanner checks (supply chain, dependency analysis)
6. Consider adding `mcp-doctor report` command for shareable HTML reports
7. Add GitHub topic tags: `mcp`, `security`, `scanner`, `audit`, `model-context-protocol`

## Key Messaging
- "Before installing an MCP server, run it through the Doctor"
- Position as the "npm meets security audit" for MCP ecosystem
- Emphasize: scan + score + compare + install + audit in one CLI
- "91+ curated servers with security scores"
- NEW: "CI/CD-ready with exit codes — gate your MCP deployments"
