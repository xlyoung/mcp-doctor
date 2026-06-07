# Changelog

All notable changes to MCP Doctor will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `mcp-doctor audit` — full security + quality audit for CI/CD pipelines with exit codes
- `mcp-doctor audit --json` — machine-readable audit output
- `mcp-doctor audit --threshold N` — configurable quality score threshold
- Tool access control bypass detection (CVE-2026-46519 pattern)
- Unconstrained parameter detection for MCP tool schemas
- Excessive permissions check (auth bypass flags, unrestricted globs)
- `SECURITY.md` — vulnerability reporting policy
- `CODE_OF_CONDUCT.md` — contributor covenant
- `CHANGELOG.md` — this file
- CI badge in README
- Reusable GitHub Action for MCP security scanning (`.github/workflows/mcp-scan-action.yml`)

### Fixed
- Fixed incorrect PyPI package name in GitHub Action (`mcp-doctor` → `mcpdoctor`)

### Changed
- Expanded test suite: CLI tests, scanner edge cases, audit command tests
- Enhanced `pyproject.toml` classifiers for better PyPI discoverability

## [0.1.0] - 2026-06-07

### Added
- Initial release
- Security scanning: prompt injection, path traversal, credential leakage, network exfiltration, SSRF, command injection
- Quality scoring (0-100) across 5 categories: Security, Maintenance, Documentation, Testing, Community
- Server comparison (`mcp-doctor compare`)
- Curated registry of 95+ MCP servers
- One-command install with safety checks (`mcp-doctor install`)
- Server search and category browsing
- Registry statistics
- JSON output mode for all commands
