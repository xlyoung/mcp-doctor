# MCP Doctor Marketing Notes

## Last run: 2026-06-07 01:00 (UTC+8)

## Current Status
- Stars: 0
- Forks: 0
- Open issues: 0
- Last push: 2026-06-07
- Registry: 85+ servers (up from 70+)

## Completed Actions
- [x] Submitted PR/issue to punkpeye/awesome-mcp-servers (issue #7489) — waiting for merge
- [x] Expanded registry from 60 → 70+ → 85+ servers (added 15 new entries this run)
- [x] Improved README with competitive comparison table
- [x] Added SEO keywords: SSRF, command injection, CI/CD, OWASP
- [x] Submitted to mcpso (chatmcp/mcpso#1) — https://github.com/chatmcp/mcpso/issues/1#issuecomment-4639924925
- [x] Added GitHub Actions CI workflow (ci.yml)
- [x] Added reusable MCP scan action (mcp-scan-action.yml)
- [x] Fixed pre-existing test_search_by_category bug

## New Registry Entries (this run)
High-star servers added:
- MindsDB (39K★), Serena (25K★), Blender MCP (22K★)
- Pipedream (11K★), CodeGraphContext (3.6K★), codebase-memory (3K★)
- MetaMCP (2.4K★), Terminator (1.5K★), DaVinci Resolve (1.2K★)
- Microsoft MCP Gateway (670★), oxvault scanner

New categories: coding agents, art/creative, aggregators, desktop automation

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
- **Only tool** combining: security scan + quality scoring + registry + comparison + install
- Competitors focus on security scanning only
- MCP Doctor is a **complete MCP server toolkit**

## Key Directories & Listings
- [ ] punkpeye/awesome-mcp-servers — issue #7489 (pending)
- [x] chatmcp/mcpso — issue #1 comment submitted
- [ ] glama.ai/mcp/servers — not yet submitted
- [ ] Docker MCP Catalog — not yet submitted
- [ ] explainx.ai leaderboard — not yet submitted
- [ ] mcpmarket.com — not yet submitted

## Relevant Discussions Found
- chatmcp/mcpso#1 — Submitted MCP Doctor entry
- punkpeye/awesome-mcp-servers#7489 — Submitted entry request (pending)
- cfgaudit/cfgaudit#248 — MCP server support (could mention mcp-doctor)
- Various CVE/security issues in MCP ecosystem

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
5. Consider adding more scanner checks (SSRF, command injection patterns)
6. Add GitHub Actions workflow for CI/CD integration ✓ (done this run)
7. Consider adding a `mcp-doctor report` command that generates shareable HTML reports

## Key Messaging
- "Before installing an MCP server, run it through the Doctor"
- Position as the "npm meets security audit" for MCP ecosystem
- Emphasize: scan + score + compare + install in one CLI
- "85+ curated servers with security scores"
