"""MCP Server Registry — curated database of known MCP servers."""
from typing import Any

# Built-in registry of well-known MCP servers
# Updated periodically by mcp-doctor auto-discovery
_REGISTRY: list[dict[str, Any]] = [
    # ── File System ──────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-filesystem", "repo": "modelcontextprotocol/servers", "category": "filesystem", "stars": 12000, "score": 92, "description": "Secure file system access with configurable allowed directories", "lang": "typescript"},
    {"name": "@anthropic/server-s3", "repo": "anthropics/anthropic-sdk-python", "category": "filesystem", "stars": 8000, "score": 85, "description": "S3 bucket access for AI agents", "lang": "python"},

    # ── Database ─────────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-postgres", "repo": "modelcontextprotocol/servers", "category": "database", "stars": 12000, "score": 90, "description": "PostgreSQL database access with read/write queries", "lang": "typescript"},
    {"name": "@modelcontextprotocol/server-sqlite", "repo": "modelcontextprotocol/servers", "category": "database", "stars": 12000, "score": 91, "description": "SQLite database access with built-in analysis", "lang": "typescript"},
    {"name": "mcp-server-mysql", "repo": "benborla/mcp-server-mysql", "category": "database", "stars": 1200, "score": 78, "description": "MySQL/MariaDB database access", "lang": "typescript"},
    {"name": "mcp-server-redis", "repo": "modelcontextprotocol/servers", "category": "database", "stars": 12000, "score": 88, "description": "Redis key-value store access", "lang": "typescript"},
    {"name": "mcp-server-qdrant", "repo": "qdrant/mcp-server-qdrant", "category": "database", "stars": 400, "score": 82, "description": "Qdrant vector database for semantic search", "lang": "python"},
    {"name": "mcp-server-clickhouse", "repo": "ClickHouse/mcp-clickhouse", "category": "database", "stars": 350, "score": 80, "description": "ClickHouse analytical database access", "lang": "python"},
    {"name": "googleapis/mcp-toolbox", "repo": "googleapis/mcp-toolbox", "category": "database", "stars": 15495, "score": 93, "description": "Google's official MCP Toolbox for Databases — PostgreSQL, MySQL, AlloyDB, Spanner, and more", "lang": "go"},
    {"name": "mcp-server-mongodb", "repo": "kiliczsh/mcp-mongo-server", "category": "database", "stars": 350, "score": 74, "description": "MongoDB database access and querying", "lang": "typescript"},
    {"name": "mcp-server-elasticsearch", "repo": "cr7258/elasticsearch-mcp-server", "category": "database", "stars": 200, "score": 72, "description": "Elasticsearch search engine access", "lang": "python"},
    {"name": "mcp-server-supabase", "repo": "supabase-community/supabase-mcp", "category": "database", "stars": 1500, "score": 85, "description": "Supabase database, auth, and storage access", "lang": "typescript"},
    {"name": "mcp-server-neon", "repo": "neondatabase/mcp-server-neon", "category": "database", "stars": 300, "score": 80, "description": "Neon serverless PostgreSQL access", "lang": "typescript"},

    # ── Web / Search ─────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-brave-search", "repo": "modelcontextprotocol/servers", "category": "web", "stars": 12000, "score": 89, "description": "Brave Search API integration", "lang": "typescript"},
    {"name": "@modelcontextprotocol/server-fetch", "repo": "modelcontextprotocol/servers", "category": "web", "stars": 12000, "score": 87, "description": "Web content fetching and conversion", "lang": "typescript"},
    {"name": "mcp-server-firecrawl", "repo": "firecrawl/firecrawl-mcp-server", "category": "web", "stars": 6506, "score": 88, "description": "Official Firecrawl MCP server — powerful web scraping and search for Cursor, Claude, and other LLM clients", "lang": "javascript"},
    {"name": "@modelcontextprotocol/server-puppeteer", "repo": "modelcontextprotocol/servers", "category": "web", "stars": 12000, "score": 85, "description": "Browser automation via Puppeteer", "lang": "typescript"},
    {"name": "microsoft/playwright-mcp", "repo": "microsoft/playwright-mcp", "category": "web", "stars": 33561, "score": 96, "description": "Official Microsoft Playwright MCP server for browser automation", "lang": "typescript"},
    {"name": "mcp-server-tavily", "repo": "tavily-ai/tavily-mcp", "category": "web", "stars": 500, "score": 82, "description": "Tavily AI-powered web search for agents", "lang": "typescript"},
    {"name": "mcp-chrome", "repo": "hangwin/mcp-chrome", "category": "web", "stars": 11853, "score": 90, "description": "Chrome extension-based MCP server for browser automation and content analysis", "lang": "typescript"},

    # ── DevOps / Git ─────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-github", "repo": "modelcontextprotocol/servers", "category": "devops", "stars": 12000, "score": 91, "description": "GitHub API: repos, issues, PRs, search", "lang": "typescript"},
    {"name": "@modelcontextprotocol/server-gitlab", "repo": "modelcontextprotocol/servers", "category": "devops", "stars": 12000, "score": 86, "description": "GitLab API integration", "lang": "typescript"},
    {"name": "mcp-server-docker", "repo": "modelcontextprotocol/servers", "category": "devops", "stars": 12000, "score": 84, "description": "Docker container management", "lang": "typescript"},
    {"name": "mcp-server-kubernetes", "repo": "Flux159/mcp-server-kubernetes", "category": "devops", "stars": 600, "score": 76, "description": "Kubernetes cluster management", "lang": "typescript"},
    {"name": "@modelcontextprotocol/server-git", "repo": "modelcontextprotocol/servers", "category": "devops", "stars": 12000, "score": 90, "description": "Local git repository operations", "lang": "python"},
    {"name": "github/github-mcp-server", "repo": "github/github-mcp-server", "category": "devops", "stars": 30469, "score": 97, "description": "GitHub's official MCP server — repos, issues, PRs, code search, gists, notifications", "lang": "typescript"},
    {"name": "mcp-server-gitlab-ci", "repo": "zereight/gitlab-mcp-server", "category": "devops", "stars": 200, "score": 70, "description": "GitLab CI/CD pipeline management", "lang": "typescript"},

    # ── Communication ────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-slack", "repo": "modelcontextprotocol/servers", "category": "communication", "stars": 12000, "score": 85, "description": "Slack workspace messaging and search", "lang": "typescript"},
    {"name": "mcp-server-discord", "repo": "SaseQ/discord-mcp", "category": "communication", "stars": 200, "score": 68, "description": "Discord bot and channel management", "lang": "typescript"},
    {"name": "mcp-server-gmail", "repo": "ShinChven/mcp-gmail", "category": "communication", "stars": 150, "score": 65, "description": "Gmail email reading and sending", "lang": "python"},
    {"name": "mcp-server-telegram", "repo": "AidenLiuZG/telegram-mcp-server", "category": "communication", "stars": 100, "score": 62, "description": "Telegram bot messaging and channel management", "lang": "python"},

    # ── Knowledge / Notes ────────────────────────────────────────
    {"name": "mcp-server-notion", "repo": "makenotion/notion-mcp-server", "category": "knowledge", "stars": 3500, "score": 88, "description": "Notion workspace page and database access", "lang": "typescript"},
    {"name": "mcp-server-obsidian", "repo": "MarkusPfS/mcp-server-obsidian", "category": "knowledge", "stars": 300, "score": 72, "description": "Obsidian vault read/write access", "lang": "python"},
    {"name": "mcp-server-memory", "repo": "modelcontextprotocol/servers", "category": "knowledge", "stars": 12000, "score": 86, "description": "Knowledge graph-based persistent memory", "lang": "typescript"},
    {"name": "mcp-server-confluence", "repo": "sooperset/mcp-atlassian", "category": "knowledge", "stars": 800, "score": 78, "description": "Atlassian Confluence and Jira access", "lang": "python"},

    # ── AI / ML ──────────────────────────────────────────────────
    {"name": "mcp-server-huggingface", "repo": "huggingface/mcp-server-hf", "category": "ai", "stars": 500, "score": 80, "description": "Hugging Face Hub model and dataset access", "lang": "python"},
    {"name": "mcp-server-ollama", "repo": "rawwerks/mcp-server-ollama", "category": "ai", "stars": 200, "score": 70, "description": "Ollama local model management", "lang": "python"},
    {"name": "mcp-server-replicate", "repo": "deepfates/mcp-server-replicate", "category": "ai", "stars": 150, "score": 68, "description": "Replicate model inference API", "lang": "python"},
    {"name": "PrefectHQ/fastmcp", "repo": "PrefectHQ/fastmcp", "category": "ai", "stars": 25506, "score": 95, "description": "The fast, Pythonic way to build MCP servers and clients", "lang": "python"},
    {"name": "mcp-server-openai", "repo": "modelcontextprotocol/servers", "category": "ai", "stars": 12000, "score": 82, "description": "OpenAI API integration for MCP", "lang": "typescript"},

    # ── Productivity ─────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-google-maps", "repo": "modelcontextprotocol/servers", "category": "productivity", "stars": 12000, "score": 83, "description": "Google Maps location and routing", "lang": "typescript"},
    {"name": "mcp-server-linear", "repo": "tacticlaunch/mcp-linear", "category": "productivity", "stars": 300, "score": 75, "description": "Linear issue tracking", "lang": "typescript"},
    {"name": "mcp-server-airtable", "repo": "domdomegg/airtable-mcp-server", "category": "productivity", "stars": 250, "score": 72, "description": "Airtable base and record management", "lang": "typescript"},
    {"name": "mcp-server-google-calendar", "repo": "nspady/google-calendar-mcp", "category": "productivity", "stars": 300, "score": 76, "description": "Google Calendar event management", "lang": "typescript"},
    {"name": "mcp-server-todoist", "repo": "abhiz123/todoist-mcp-server", "category": "productivity", "stars": 150, "score": 68, "description": "Todoist task management", "lang": "typescript"},

    # ── Cloud ────────────────────────────────────────────────────
    {"name": "@modelcontextprotocol/server-everything", "repo": "modelcontextprotocol/servers", "category": "reference", "stars": 12000, "score": 88, "description": "Reference MCP server with all features", "lang": "typescript"},
    {"name": "mcp-server-aws", "repo": "alexfields/aws-mcp-server", "category": "cloud", "stars": 100, "score": 65, "description": "AWS service management via MCP", "lang": "python"},

    # ── Security ─────────────────────────────────────────────────
    {"name": "mcp-server-semgrep", "repo": "semgrep/mcp", "category": "security", "stars": 200, "score": 82, "description": "Semgrep code security scanning via MCP", "lang": "python"},
    {"name": "mcp-server-nvd", "repo": "willclarktech/mcp-server-nvd", "category": "security", "stars": 50, "score": 68, "description": "NVD (National Vulnerability Database) CVE lookup", "lang": "typescript"},

    # ── Design ───────────────────────────────────────────────────
    {"name": "Figma-Context-MCP", "repo": "GLips/Figma-Context-MCP", "category": "design", "stars": 15007, "score": 93, "description": "Figma layout information for AI coding agents like Cursor", "lang": "typescript"},

    # ── Headless CMS / Content ────────────────────────────────
    {"name": "mcp-server-strapi", "repo": "strapi/mcp-server-strapi", "category": "cms", "stars": 100, "score": 66, "description": "Strapi headless CMS content management", "lang": "typescript"},

    # ── System / Desktop ──────────────────────────────────────
    {"name": "DesktopCommanderMCP", "repo": "wonderwhy-er/DesktopCommanderMCP", "category": "system", "stars": 6114, "score": 78, "description": "Execute terminal commands, manage files and processes from MCP clients", "lang": "typescript"},
    {"name": "Windows-MCP", "repo": "CursorTouch/Windows-MCP", "category": "system", "stars": 5879, "score": 75, "description": "Windows OS automation — UI interaction, app control, clipboard, and screen capture", "lang": "python"},

    # ── Reverse Engineering / Binary ──────────────────────────
    {"name": "GhidraMCP", "repo": "LaurieWired/GhidraMCP", "category": "security", "stars": 9137, "score": 88, "description": "Ghidra reverse engineering via MCP — decompile, analyze, and explore binaries with AI", "lang": "java"},

    # ── Communication (new) ───────────────────────────────────
    {"name": "whatsapp-mcp", "repo": "lharries/whatsapp-mcp", "category": "communication", "stars": 5735, "score": 76, "description": "WhatsApp messaging integration — send, receive, and search messages", "lang": "python"},

    # ── Mobile / iOS Dev ──────────────────────────────────────
    {"name": "XcodeBuildMCP", "repo": "getsentry/XcodeBuildMCP", "category": "devops", "stars": 5844, "score": 85, "description": "Xcode project build, test, and run for iOS/macOS development via MCP", "lang": "typescript"},

    # ── Developer Tools ───────────────────────────────────────
    {"name": "mcp-inspector", "repo": "modelcontextprotocol/inspector", "category": "devtools", "stars": 10011, "score": 92, "description": "Official MCP inspector — debug and test MCP servers interactively", "lang": "typescript"},
    {"name": "git-mcp", "repo": "idosal/git-mcp", "category": "devtools", "stars": 8142, "score": 86, "description": "Instant MCP server for any GitHub repo — code search and documentation retrieval", "lang": "typescript"},

    # ── Workflow / Automation ─────────────────────────────────────
    {"name": "activepieces", "repo": "activepieces/activepieces", "category": "automation", "stars": 22585, "score": 90, "description": "AI Agents & MCP workflow automation platform with ~400 built-in MCP servers for AI agents", "lang": "typescript"},

    # ── Framework ─────────────────────────────────────────────────
    {"name": "mcp-use", "repo": "mcp-use/mcp-use", "category": "framework", "stars": 10061, "score": 89, "description": "Fullstack MCP framework to develop MCP Apps for ChatGPT/Claude and MCP Servers for AI Agents", "lang": "typescript"},

    # ── Cloud / AWS ──────────────────────────────────────────────
    {"name": "awslabs-mcp", "repo": "awslabs/mcp", "category": "cloud", "stars": 9219, "score": 88, "description": "Open source MCP servers for AWS — Lambda, S3, DynamoDB, CloudWatch, and more", "lang": "python"},

    # ── Browser Automation (new) ─────────────────────────────────
    {"name": "BrowserMCP", "repo": "BrowserMCP/mcp", "category": "web", "stars": 6630, "score": 85, "description": "Browser MCP server — allows AI applications to control your browser via the Model Context Protocol", "lang": "typescript"},
    {"name": "bb-browser", "repo": "epiral/bb-browser", "category": "web", "stars": 5689, "score": 82, "description": "CLI + MCP server for AI agents to control Chrome with your login state — your browser is the API", "lang": "typescript"},

    # ── Registry / Discovery ─────────────────────────────────────
    {"name": "mcp-registry", "repo": "modelcontextprotocol/registry", "category": "devtools", "stars": 6894, "score": 87, "description": "Official community-driven registry service for Model Context Protocol (MCP) servers", "lang": "go"},

    # ── Document Processing ──────────────────────────────────────
    {"name": "kreuzberg", "repo": "kreuzberg-dev/kreuzberg", "category": "productivity", "stars": 8449, "score": 84, "description": "Polyglot document intelligence framework with Rust core — extract text, metadata, and structured info from 97+ formats via MCP", "lang": "rust"},

    # ── Security (new) ──────────────────────────────────────────
    {"name": "mcp-audit", "repo": "Norbi0801/mcp-audit", "category": "security", "stars": 150, "score": 75, "description": "Security auditing tool for MCP servers — 19 rules covering OWASP MCP Top 10, SARIF output for CI/CD", "lang": "rust"},
    {"name": "mcpsec", "repo": "mcp-shark/mcpsec", "category": "security", "stars": 100, "score": 72, "description": "MCP server compliance scanner — validates against MCP spec, OWASP Top 10, and FastMCP baseline", "lang": "python"},
    {"name": "oxvault-scanner", "repo": "oxvault/scanner", "category": "security", "stars": 3, "score": 70, "description": "Go-based MCP security scanner — 12/12 CVE detection, SSRF/path traversal/rug pull checks, zero dependencies", "lang": "go"},

    # ── Coding Agents (new) ────────────────────────────────────
    {"name": "serena", "repo": "oraios/serena", "category": "ai", "stars": 25001, "score": 95, "description": "Fully-featured coding agent using language servers for symbolic code operations — the IDE for your agent", "lang": "python"},
    {"name": "codebase-memory-mcp", "repo": "deusdata/codebase-memory-mcp", "category": "devtools", "stars": 3008, "score": 86, "description": "High-performance code intelligence MCP server — indexes codebases into a persistent knowledge graph, 159 languages, sub-ms queries", "lang": "c"},
    {"name": "CodeGraphContext", "repo": "CodeGraphContext/CodeGraphContext", "category": "devtools", "stars": 3624, "score": 85, "description": "MCP server that indexes local code into a graph database to provide context to AI assistants with graphical code exploration", "lang": "python"},

    # ── Art / Creative (new) ──────────────────────────────────
    {"name": "blender-mcp", "repo": "ahujasid/blender-mcp", "category": "design", "stars": 22395, "score": 90, "description": "MCP server for working with Blender — 3D modeling, rendering, and scene manipulation via AI", "lang": "python"},
    {"name": "davinci-resolve-mcp", "repo": "samuelgursky/davinci-resolve-mcp", "category": "design", "stars": 1186, "score": 82, "description": "MCP server integration for DaVinci Resolve Studio — video editing, color grading, and media management", "lang": "python"},

    # ── Aggregators / Middleware (new) ─────────────────────────
    {"name": "metamcp", "repo": "metatool-ai/metamcp", "category": "devtools", "stars": 2382, "score": 82, "description": "Unified middleware MCP server that manages your MCP connections with GUI — aggregator, orchestrator, and gateway", "lang": "typescript"},
    {"name": "mcp-gateway", "repo": "microsoft/mcp-gateway", "category": "devtools", "stars": 670, "score": 85, "description": "Microsoft's MCP Gateway — reverse proxy and management layer for MCP servers with session-aware routing in Kubernetes", "lang": "typescript"},

    # ── Automation / Integration (new) ────────────────────────
    {"name": "pipedream-mcp", "repo": "PipedreamHQ/pipedream", "category": "automation", "stars": 11440, "score": 88, "description": "Connect 2,500+ APIs with 8,000+ prebuilt tools and manage MCP servers for your users", "lang": "typescript"},
    {"name": "mindsdb-mcp", "repo": "mindsdb/mindsdb", "category": "database", "stars": 39253, "score": 92, "description": "Connect and unify data across various platforms and databases with MindsDB as a single MCP server", "lang": "python"},

    # ── Desktop Automation (new) ──────────────────────────────
    {"name": "terminator", "repo": "mediar-ai/terminator", "category": "system", "stars": 1518, "score": 80, "description": "Desktop GUI automation using accessibility APIs — control Windows, macOS, and Linux apps without vision models", "lang": "rust"},

    # ── Web / Browser DevTools (new) ─────────────────────────
    {"name": "chrome-devtools-mcp", "repo": "ChromeDevTools/chrome-devtools-mcp", "category": "web", "stars": 42991, "score": 97, "description": "Official Chrome DevTools MCP server for coding agents — inspect, debug, and automate Chrome from your AI assistant", "lang": "typescript"},

    # ── Workflow / n8n (new) ─────────────────────────────────
    {"name": "n8n-mcp", "repo": "czlonkowski/n8n-mcp", "category": "automation", "stars": 21580, "score": 90, "description": "MCP server for Claude Desktop / Cursor / Windsurf to build n8n workflows — 500+ node types, workflow CRUD, AI-assisted automation", "lang": "typescript"},

    # ── Token Optimization (new) ────────────────────────────
    {"name": "headroom", "repo": "chopratejas/headroom", "category": "ai", "stars": 15690, "score": 88, "description": "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM — 60-95% fewer tokens, same answers", "lang": "python"},

    # ── Social Media (new) ──────────────────────────────────
    {"name": "xiaohongshu-mcp", "repo": "xpzouying/xiaohongshu-mcp", "category": "web", "stars": 14014, "score": 85, "description": "MCP server for Xiaohongshu (Little Red Book) — search, browse, and interact with China's largest lifestyle platform", "lang": "python"},

    # ── Framework / FastAPI (new) ───────────────────────────
    {"name": "fastapi-mcp", "repo": "tadata-org/fastapi_mcp", "category": "framework", "stars": 11897, "score": 89, "description": "Expose FastAPI endpoints as MCP tools with automatic schema generation and OAuth support", "lang": "python"},

    # ── Design / Design System (new) ─────────────────────────
    {"name": "design-extract", "repo": "Manavarya09/design-extract", "category": "design", "stars": 3074, "score": 85, "description": "Extract any website's complete design system — DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter), Tailwind v4, Figma variables", "lang": "typescript"},

    # ── Search / Aggregator (new) ────────────────────────────
    {"name": "anysearch-mcp-server", "repo": "anysearch-ai/anysearch-mcp-server", "category": "web", "stars": 1023, "score": 78, "description": "Unified real-time search engine skill for AI agents — one MCP server for multiple search providers", "lang": "typescript"},

    # ── Security / CVE Intelligence (new) ────────────────────
    {"name": "cve-mcp-server", "repo": "mukul975/cve-mcp-server", "category": "security", "stars": 952, "score": 86, "description": "Production-grade MCP server with 27 security intelligence tools across 21 APIs — CVE lookup, EPSS scoring, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal", "lang": "python"},

    # ── Knowledge / Memory (new) ─────────────────────────────
    {"name": "stash", "repo": "alash3al/stash", "category": "knowledge", "stars": 710, "score": 80, "description": "Persistent memory layer for AI agents — episodes, facts, and working context stored in Postgres with MCP server. Self-hosted, single binary", "lang": "go"},

    # ── Security / Pentesting (new) ──────────────────────────
    {"name": "pentest-ai", "repo": "0xSteph/pentest-ai", "category": "security", "stars": 598, "score": 76, "description": "Offensive-security MCP server with 205 wrapped tools, 17 specialist agents, and 60 SPA-aware probes for OWASP Top 10. CLI + MCP, BYO LLM", "lang": "python"},

    # ── Cloud / AWS Official (new) ───────────────────────────
    {"name": "agent-toolkit-for-aws", "repo": "aws/agent-toolkit-for-aws", "category": "cloud", "stars": 803, "score": 88, "description": "Official AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS", "lang": "python"},

    # ── Multi-Model Aggregators (new) ──────────────────────────
    {"name": "pal-mcp-server", "repo": "BeehiveInnovations/pal-mcp-server", "category": "ai", "stars": 11588, "score": 87, "description": "Multi-model MCP aggregator — Claude Code, GeminiCLI, CodexCLI + Gemini/OpenAI/OpenRouter/Azure/Grok/Ollama working as one", "lang": "python"},

    # ── Cybersecurity / Pentesting (new) ──────────────────────
    {"name": "hexstrike-ai", "repo": "0x4m4/hexstrike-ai", "category": "security", "stars": 9376, "score": 80, "description": "HexStrike AI MCP Agents — 150+ cybersecurity tools for automated pentesting, vulnerability discovery, and bug bounty automation", "lang": "python"},
]


def get_registry() -> list[dict[str, Any]]:
    """Return the full MCP server registry."""
    return _REGISTRY.copy()


def search_servers(query: str) -> list[dict[str, Any]]:
    """Search servers by name, description, or category."""
    q = query.lower()
    return [
        s for s in _REGISTRY
        if q in s.get("name", "").lower()
        or q in s.get("description", "").lower()
        or q in s.get("category", "").lower()
    ]
