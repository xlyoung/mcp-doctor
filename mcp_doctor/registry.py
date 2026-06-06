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
    {"name": "mcp-server-firecrawl", "repo": "firecrawl/mcp-server", "category": "web", "stars": 5000, "score": 88, "description": "Web scraping with Firecrawl", "lang": "typescript"},
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
