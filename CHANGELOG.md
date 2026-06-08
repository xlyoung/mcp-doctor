# Changelog

All notable changes to MCP Doctor will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `--ci` flag for `mcp-doctor scan` — CI-friendly mode with JSON output and exit codes
- Unsafe deserialization detection (pickle, yaml.load, marshal, shelve, jsonpickle)
- Dynamic import detection (__import__, importlib, require with user input)
- Log injection detection (user input in log statements)
- `.github/workflows/security-scan.yml` — ready-to-use CI workflow
- New test suite for scanner security checks (`test_scanner_new_checks.py`)

### Changed
- Improved `mcp-scan-action.yml` with `--ci` flag and `fail_on_high` option
- Security engine count: 9 → 12 detection engines

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
