# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in MCP Doctor, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email: **security@xlyoung.dev** (or open a [GitHub Security Advisory](https://github.com/xlyoung/mcp-doctor/security/advisories/new)).

### What to include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response timeline

- **Acknowledgment**: within 48 hours
- **Initial assessment**: within 1 week
- **Fix & release**: within 2 weeks (for confirmed vulnerabilities)

## Scope

MCP Doctor is a security scanning tool. The following are considered in-scope:

- Code execution vulnerabilities in MCP Doctor itself
- Dependency vulnerabilities in our supply chain
- Injection attacks via malicious server names or registry data
- Denial of service via crafted inputs

## Out of Scope

- Vulnerabilities in the MCP servers that MCP Doctor *scans* (report those to the server maintainers)
- Social engineering attacks
- Issues requiring physical access to the user's machine

## Recognition

We credit all responsible disclosures in our CHANGELOG. Thank you for helping keep the MCP ecosystem safe!
