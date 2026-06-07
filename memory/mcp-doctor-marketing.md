# MCP Doctor Marketing Notes

## Last run: 2026-06-07 06:15 (UTC+8)

## Current Status
- Stars: 0
- Forks: 0
- Open issues: 0
- Last push: 2026-06-07
- Registry: 100+ servers (up from 95+)
- Security checks: 8 categories (prompt injection, path traversal, credential leakage, network exfiltration, SSRF, command injection, supply chain, excessive permissions)

## Completed Actions (this run)
- [x] Added 2 new high-star servers to registry:
  - pal-mcp-server (11.6K★) — Multi-model MCP aggregator
  - hexstrike-ai (9.4K★) — 150+ cybersecurity pentesting tools
- [x] Resolved merge conflicts and pushed changes
- [x] Community outreach: Submitted to 3 new awesome lists:
  - yzfly/Awesome-MCP-ZH#268 (7.2K★ list, Chinese MCP directory)
  - YuzeHao2023/Awesome-MCP-Servers#301 (1K★ list)
  - TensorBlock/awesome-mcp-servers#668 (728★ list)
  - MobinX/awesome-mcp-list#303 (878★ list)
- [x] Researched competitive landscape (MCPScan, mcpaudit, jsandov/mcp-audit, sahiloj/MCPScan)
- [x] Verified HN discussion about MCP-Scanner (Cisco) — noted MCP Doctor's differentiator

## Previous Actions (still active)
- [x] Submitted PR/issue to punkpeye/awesome-mcp-servers (issue #7489) — waiting for merge
- [x] Submitted to mcpso (chatmcp/mcpso#1)
- [x] Submitted to Puliczek/awesome-mcp-security (issue #185) — waiting for merge
- [x] Added GitHub Actions CI workflow (ci.yml)
- [x] Added reusable MCP scan action (mcp-scan-action.yml)
- [x] Community outreach: PrefectHQ/fastmcp#4244, AIAnytime/Awesome-MCP-Server#35

## Registry Growth
- Started: 60 servers → 70+ → 85+ → 91+ → 95+ → now 100+ servers
- 22+ categories including: web, database, devops, ai, automation, framework, security, design, pentesting, aggregators

## Competing Tools (MCP Security Space)
- **MCPScan (sahiloj)** — TypeScript, 8 check categories, offensive security, MITRE ATT&CK
- **mcp-audit (Norbi0801)** — Rust, 19 rules, AGPL-3.0, OWASP MCP Top 10
- **mcpaudit (piiiico)** — npm/npx, static scanner, multi-language, 14 patterns
- **MCPSec (mcp-shark)** — Compliance scanner, MCP spec + OWASP
- **mcp-shield (GaboITB)** — Python, 17 detectors, Docker sandbox
- **mcpscan (obielin)** — Python, 8 rules, zero deps
- **mcp-security-scanner (TreRB)** — Node, 8 checks, static audit
- **mcp-security-scan (agentgraph-co)** — npm, static + dynamic, trust scores
- **mcp-security-auditor (prabhubng)** — npm, 7 analyzers
- **oxvault/scanner** — Go, 12/12 CVE detection, zero deps
- **jsandov/mcp-audit** — Python, 7 categories, attack graph dashboard
- **kryptonomeai-cloud/mcpscan** — Python, 10 modules, 40+ rules

## MCP Doctor's Unique Position
- **Only tool** combining: security scan + quality scoring + registry + comparison + install + CI/CD audit
- Competitors focus on security scanning only
- MCP Doctor is a **complete MCP server toolkit**
- `audit` command makes it CI/CD pipeline-ready with exit codes
- 100+ curated servers with quality scores — no competitor has this

## Key Directories & Listings
- [ ] punkpeye/awesome-mcp-servers — issue #7489 (pending)
- [x] chatmcp/mcpso — issue #1 comment submitted
- [x] Puliczek/awesome-mcp-security — issue #185 (pending)
- [x] yzfly/Awesome-MCP-ZH — issue #268 (submitted)
- [x] YuzeHao2023/Awesome-MCP-Servers — issue #301 (submitted)
- [x] TensorBlock/awesome-mcp-servers — issue #668 (submitted)
- [x] MobinX/awesome-mcp-list — issue #303 (submitted)
- [ ] glama.ai/mcp/servers — not yet submitted
- [ ] Docker MCP Catalog — not yet submitted
- [ ] explainx.ai leaderboard — not yet submitted
- [ ] mcpmarket.com — not yet submitted
- [ ] GitHub Actions Marketplace — not yet submitted

## MCP Ecosystem Context (June 2026)
- MCP has ~97M monthly SDK downloads
- ~9,400-17,000+ public MCP servers across registries
- MCP 2026-07-28 RC: stateless transport, 22 SEPs
- 30+ MCP-related CVEs filed in H1 2026
- Major adoption: Claude, ChatGPT, Gemini, VS Code, Cursor
- Enterprise readiness is top priority in 2026 roadmap
- HN discussion: MCP-Scanner (Cisco) vs Invariant Labs mcp-scan — toxic flow analysis

## Next Steps
1. Monitor all submitted issues for merge/acceptance
2. Submit to glama.ai, mcpmarket.com, explainx.ai directories
3. Submit MCP Doctor GitHub Action to Actions Marketplace
4. Add `mcp-doctor report` command for shareable HTML reports
5. Consider adding "toxic flow" detection (cross-server analysis) — differentiator vs competitors
6. Search Reddit/V2EX for MCP security discussions (Strategy D)
7. Find 2-3 more relevant GitHub issues to recommend MCP Doctor naturally
8. Add more scanner checks (supply chain, dependency analysis)

## Key Messaging
- "Before installing an MCP server, run it through the Doctor"
- Position as the "npm meets security audit" for MCP ecosystem
- Emphasize: scan + score + compare + install + audit in one CLI
- "100+ curated servers with security scores"
- "CI/CD-ready with exit codes — gate your MCP deployments"
- "Unlike security-only scanners, MCP Doctor gives you the full picture: security + quality + registry"
