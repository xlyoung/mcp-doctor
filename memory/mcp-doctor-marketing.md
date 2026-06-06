# MCP Doctor Marketing Notes

## Last run: 2026-06-07 10:00 (UTC+8)

## Current Status
- Stars: 0
- Forks: 0
- Open issues: 0
- Last push: 2026-06-07
- Registry: 97+ servers (up from 91+)
- Security checks: 8 categories (added unconstrained params, tool access control bypass)

## Completed Actions (this run)
- [x] **Strategy A — New scanner checks:**
  - `_check_unconstrained_params`: detects string params without maxLength/pattern/enum constraints (ref: modelcontextprotocol/servers#3537)
  - `_check_tool_access_control`: detects presentation-layer-only filtering bypass (ref: CVE-2026-46519 in mcp-server-kubernetes)
  - All 7 tests pass
- [x] **Strategy B — Registry expansion (91+ → 97+):**
  - design-extract (3K★) — website design system extraction
  - anysearch-mcp-server (1K★) — unified search for AI agents
  - cve-mcp-server (952★) — CVE/security intelligence (27 tools, 21 APIs)
  - agent-toolkit-for-aws (803★) — official AWS MCP toolkit
  - stash (710★) — persistent memory layer for AI agents
  - pentest-ai (598★) — offensive security with 205 tools
- [x] **Strategy C — Community outreach:**
  - Commented on modelcontextprotocol/servers#4143 (SSRF protection, cloud metadata exfiltration) — naturally recommended MCP Doctor's SSRF detection
  - Commented on modelcontextprotocol/servers#3537 (unconstrained string parameters) — referenced new scanner check
- [x] **Strategy D — Ecosystem research:**
  - Found HN thread #47356600 "MCP Security 2026: 30 CVEs in 60 Days" — active discussion
  - Found HN thread #47692889 "Show HN: MCP-fence" — MCP firewall, complementary to MCP Doctor
  - Found HN thread #47367404 "Show HN: MCPS" — cryptographic identity for MCP agents
  - Found HN thread #47138022 "We audited both MCP SDKs" — boundary-crossing vulnerabilities
- [x] Updated README security checks section

## Previous Actions (still active)
- [x] Submitted PR/issue to punkpeye/awesome-mcp-servers (issue #7489) — waiting for merge
- [x] Submitted to mcpso (chatmcp/mcpso#1)
- [x] Added GitHub Actions CI workflow (ci.yml)
- [x] Added reusable MCP scan action (mcp-scan-action.yml)

## Registry Growth
- Started: 60 servers → 70+ → 85+ → 91+ → now 97+ servers
- 20+ categories including: web, database, devops, ai, automation, framework, security, design

## Competing Tools (MCP Security Space)
- **mcp-shield** (GaboITB) — Python, 17 detectors, Docker sandbox, zero deps (NEW competitor)
- **velox-mcp-audit** (veloxlabsio) — Python, 6 checks, AST scanning, early alpha (NEW competitor)
- **mcpaudit** (piiiico) — npm/npx, static scanner, multi-language
- **MCPScan** (sahiloj) — Node, 8 check categories, offensive auditor (NEW competitor)
- **mcp-audit** (jsandov) — Python, 7 categories, attack graph dashboard
- **mcp-audit** (Norbi0801) — Rust, 19 rules, AGPL-3.0, OWASP MCP Top 10
- **MCPSec** (mcp-shark) — Compliance scanner, MCP spec + OWASP
- **oxvault/scanner** — Go, 12/12 CVE detection, zero deps

## MCP Doctor's Unique Position
- **Only tool** combining: security scan + quality scoring + registry + comparison + install + CI/CD audit
- Competitors focus on security scanning only
- MCP Doctor is a **complete MCP server toolkit**
- New checks (unconstrained params, tool access control) directly address community-reported issues

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
- **modelcontextprotocol/servers#4143** — Commented on SSRF protection (NEW)
- **modelcontextprotocol/servers#3537** — Commented on unconstrained string parameters (NEW)

## HN Discussions Worth Monitoring
- #47356600 — "MCP Security 2026: 30 CVEs in 60 Days" (active, security-focused)
- #47692889 — "Show HN: MCP-fence" (MCP firewall, complementary tool)
- #47367404 — "Show HN: MCPS" (cryptographic identity layer)
- #47138022 — "We audited both MCP SDKs" (boundary-crossing vulns)

## MCP Ecosystem Context (June 2026)
- MCP has ~97M monthly SDK downloads
- ~9,400-17,000+ public MCP servers across registries
- MCP 2026-07-28 RC: stateless transport, 22 SEPs
- 30+ MCP-related CVEs filed in H1 2026
- Major adoption: Claude, ChatGPT, Gemini, VS Code, Cursor
- Enterprise readiness is top priority in 2026 roadmap
- New competitors emerging weekly — differentiation through completeness is key

## Next Steps
1. Monitor awesome-mcp-servers issue #7489 for merge
2. Submit to glama.ai, mcpmarket.com, explainx.ai directories
3. Add `mcp-doctor report` command for shareable HTML reports
4. Consider adding dependency CVE scanning to scanner
5. Search V2EX/Reddit for Chinese-language MCP discussions (xiaohongshu-mcp angle)
6. Add more scanner checks (OAuth conformance, transport security)
7. Consider "MCP Doctor Verified" badge for well-scored servers

## Key Messaging
- "Before installing an MCP server, run it through the Doctor"
- Position as the "npm meets security audit" for MCP ecosystem
- Emphasize: scan + score + compare + install + audit in one CLI
- "97+ curated servers with security scores"
- NEW: "Detects unconstrained parameters and tool access control bypasses"
- NEW: "CI/CD-ready with exit codes — gate your MCP deployments"
