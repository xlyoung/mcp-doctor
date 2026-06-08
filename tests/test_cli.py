"""Tests for MCP Doctor CLI."""
import json
from click.testing import CliRunner
from mcp_doctor.cli import main


runner = CliRunner()


def test_cli_help():
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "MCP Doctor" in result.output


def test_scan_help():
    result = runner.invoke(main, ["scan", "--help"])
    assert result.exit_code == 0
    assert "security" in result.output.lower()


def test_score_help():
    result = runner.invoke(main, ["score", "--help"])
    assert result.exit_code == 0
    assert "quality" in result.output.lower() or "score" in result.output.lower()


def test_compare_help():
    result = runner.invoke(main, ["compare", "--help"])
    assert result.exit_code == 0
    assert "compare" in result.output.lower()


def test_audit_help():
    result = runner.invoke(main, ["audit", "--help"])
    assert result.exit_code == 0
    assert "threshold" in result.output.lower()


def test_list_help():
    result = runner.invoke(main, ["list", "--help"])
    assert result.exit_code == 0
    assert "category" in result.output.lower()


def test_stats():
    result = runner.invoke(main, ["stats"])
    assert result.exit_code == 0
    assert "Registry" in result.output or "servers" in result.output.lower()


def test_search():
    result = runner.invoke(main, ["search", "database"])
    assert result.exit_code == 0


def test_search_no_results():
    result = runner.invoke(main, ["search", "zzz_nonexistent_server_xyz"])
    assert result.exit_code == 0
    assert "No servers found" in result.output


def test_list_with_category():
    result = runner.invoke(main, ["list", "--category", "database", "--limit", "5"])
    assert result.exit_code == 0


def test_scan_json_output():
    result = runner.invoke(main, ["scan", "modelcontextprotocol/servers", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "issues" in data
    assert "critical" in data


def test_score_json_output():
    result = runner.invoke(main, ["score", "modelcontextprotocol/servers", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "total" in data
    assert 0 <= data["total"] <= 100


def test_compare_json_output():
    result = runner.invoke(main, [
        "compare", "modelcontextprotocol/servers",
        "benborla/mcp-server-mysql", "--json",
    ])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "server_a" in data
    assert "server_b" in data


def test_audit_json_pass():
    result = runner.invoke(main, [
        "audit", "modelcontextprotocol/servers", "--json", "--threshold", "0",
    ])
    # If network is available, exit 0. If GitHub API is down, threshold 0 still passes
    # unless there are critical issues. Just verify JSON output is valid.
    data = json.loads(result.output)
    assert "passed" in data
    assert "score" in data
    assert "issues" in data


def test_audit_threshold_fail():
    """Audit with impossibly high threshold should fail."""
    result = runner.invoke(main, [
        "audit", "modelcontextprotocol/servers", "--threshold", "99", "--json",
    ])
    assert result.exit_code == 1
    data = json.loads(result.output)
    assert data["passed"] is False


def test_install_help():
    result = runner.invoke(main, ["install", "--help"])
    assert result.exit_code == 0
    assert "--force" in result.output


def test_scan_ci_flag_help():
    result = runner.invoke(main, ["scan", "--help"])
    assert result.exit_code == 0
    assert "--ci" in result.output


def test_scan_ci_json_output():
    """--ci flag should produce JSON output."""
    result = runner.invoke(main, ["scan", "modelcontextprotocol/servers", "--ci"])
    # Should produce JSON output (exit code depends on findings)
    assert result.exit_code in (0, 1)
    # Output starts with JSON — find the first { and parse from there
    import json
    output = result.output
    json_start = output.find("{")
    assert json_start >= 0, f"No JSON found in output: {output[:200]}"
    # Find the matching closing brace
    brace_count = 0
    json_end = json_start
    for i, ch in enumerate(output[json_start:], json_start):
        if ch == "{":
            brace_count += 1
        elif ch == "}":
            brace_count -= 1
            if brace_count == 0:
                json_end = i + 1
                break
    data = json.loads(output[json_start:json_end])
    assert "issues" in data
