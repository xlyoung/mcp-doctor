"""MCP Doctor CLI — Scan, Score, Install MCP Servers."""
import sys
import click
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from mcp_doctor.registry import get_registry, search_servers
from mcp_doctor.scanner import scan_server
from mcp_doctor.scorer import score_server

console = Console()


@click.group()
@click.version_option(package_name="mcp-doctor")
def main():
    """\[emoji] MCP Doctor — Scan, Score, Install MCP Servers with confidence."""
    pass


@main.command()
@click.argument("server")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def scan(server: str, as_json: bool):
    """Scan an MCP server for security vulnerabilities."""
    result = scan_server(server)
    if as_json:
        click.echo(json.dumps(result, indent=2))
    else:
        _render_scan(result)


@main.command()
@click.argument("server")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def score(server: str, as_json: bool):
    """Score an MCP server's quality (0-100)."""
    result = score_server(server)
    if as_json:
        click.echo(json.dumps(result, indent=2))
    else:
        _render_score(result)


@main.command(name="list")
@click.option("--category", "-c", help="Filter by category")
@click.option("--sort", "-s", default="score", type=click.Choice(["score", "stars", "name", "updated"]))
@click.option("--limit", "-n", default=20, type=int)
def list_cmd(category: str, sort: str, limit: int):
    """List MCP servers from the registry."""
    registry = get_registry()
    servers = registry
    if category:
        servers = [s for s in servers if s.get("category", "").lower() == category.lower()]
    reverse = sort != "name"
    servers.sort(key=lambda s: s.get(sort, 0), reverse=reverse)
    _render_table(servers[:limit])


@main.command()
@click.argument("query")
def search(query: str):
    """Search for MCP servers by name or description."""
    results = search_servers(query)
    if not results:
        console.print(f"[yellow]No servers found for:[/yellow] {query}")
        return
    _render_table(results)


@main.command()
@click.argument("server")
@click.option("--force", is_flag=True, help="Skip critical issue check")
def install(server: str, force: bool):
    """Scan + score + install an MCP server."""
    console.print(f"\n[bold]Running pre-install checks for:[/bold] {server}\n")

    # Step 1: Scan
    console.print("[bold cyan]\u276f Security Scan[/bold cyan]")
    scan_result = scan_server(server)
    _render_scan(scan_result)

    if scan_result.get("critical", 0) > 0 and not force:
        console.print("\n[red bold]\u2716 CRITICAL issues found. Install blocked.[/red bold]")
        console.print("[dim]Use --force to override (not recommended)[/dim]")
        sys.exit(1)

    # Step 2: Score
    console.print("\n[bold cyan]\u276f Quality Score[/bold cyan]")
    score_result = score_server(server)
    _render_score(score_result)

    if score_result.get("total", 0) < 30:
        console.print("\n[yellow]\u26a0 Score below 30. Proceed with caution.[/yellow]")

    # Step 3: Info
    console.print(f"\n[green]\u2714 {server} passed pre-install checks[/green]")
    console.print(f"[dim]Add to your MCP config manually or run:[/dim]")
    console.print(f"  [bold]claude mcp add {server}[/bold]")


@main.command()
@click.argument("server_a")
@click.argument("server_b")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def compare(server_a: str, server_b: str, as_json: bool):
    """Compare two MCP servers side-by-side."""
    console.print(f"\n[bold]Comparing:[/bold] {server_a} vs {server_b}\n")

    score_a = score_server(server_a)
    score_b = score_server(server_b)
    scan_a = scan_server(server_a)
    scan_b = scan_server(server_b)

    if as_json:
        click.echo(json.dumps({
            "server_a": {"name": server_a, "score": score_a, "scan": scan_a},
            "server_b": {"name": server_b, "score": score_b, "scan": scan_b},
        }, indent=2))
        return

    # Side-by-side comparison table
    table = Table(show_header=True, header_style="bold magenta", title="MCP Server Comparison")
    table.add_column("Metric", style="bold", width=20)
    table.add_column(server_a, justify="center", width=20)
    table.add_column(server_b, justify="center", width=20)
    table.add_column("Winner", justify="center", width=12)

    # Overall score
    ta, tb = score_a.get("total", 0), score_b.get("total", 0)
    winner = "\u2b50" if ta > tb else "\u2b50" if tb > ta else "\u2796"
    table.add_row(
        "Overall Score",
        f"[{'green' if ta>=70 else 'yellow' if ta>=40 else 'red'}]{ta}/100[/{'green' if ta>=70 else 'yellow' if ta>=40 else 'red'}]",
        f"[{'green' if tb>=70 else 'yellow' if tb>=40 else 'red'}]{tb}/100[/{'green' if tb>=70 else 'yellow' if tb>=40 else 'red'}]",
        server_a if ta > tb else server_b if tb > ta else "Tie",
    )

    # Category scores
    cats_a = score_a.get("categories", {})
    cats_b = score_b.get("categories", {})
    for cat in ["Security", "Maintenance", "Documentation", "Testing", "Community"]:
        sa = cats_a.get(cat, {}).get("score", 0)
        sb = cats_b.get(cat, {}).get("score", 0)
        table.add_row(
            cat,
            str(sa),
            str(sb),
            server_a if sa > sb else server_b if sb > sa else "Tie",
        )

    # Security issues
    ia, ib = len(scan_a.get("issues", [])), len(scan_b.get("issues", []))
    table.add_row(
        "Security Issues",
        f"[red]{ia}[/red]" if ia > 0 else "[green]0[/green]",
        f"[red]{ib}[/red]" if ib > 0 else "[green]0[/green]",
        server_a if ia < ib else server_b if ib < ia else "Tie",
    )

    console.print(table)

    # Recommendation
    if ta > tb + 10:
        console.print(f"\n[green]\u2714 Recommendation: {server_a}[/green] (score {ta} vs {tb})")
    elif tb > ta + 10:
        console.print(f"\n[green]\u2714 Recommendation: {server_b}[/green] (score {tb} vs {ta})")
    else:
        console.print(f"\n[yellow]\u26a0 Both servers are comparable. Choose based on your specific needs.[/yellow]")


@main.command()
@click.argument("server")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
@click.option("--threshold", "-t", default=50, type=int, help="Minimum score to pass (default: 50)")
@click.option("--fail-on-critical", is_flag=True, default=True, help="Fail if critical issues found (default: true)")
def audit(server: str, as_json: bool, threshold: int, fail_on_critical: bool):
    """Run a full security + quality audit. Designed for CI/CD pipelines."""
    scan_result = scan_server(server)
    score_result = score_server(server)

    critical = scan_result.get("critical", 0)
    high = scan_result.get("high", 0)
    total_score = score_result.get("total", 0)
    passed = total_score >= threshold and not (fail_on_critical and critical > 0)

    report = {
        "server": server,
        "passed": passed,
        "score": total_score,
        "threshold": threshold,
        "issues": {
            "critical": critical,
            "high": high,
            "medium": scan_result.get("medium", 0),
            "low": scan_result.get("low", 0),
            "total": len(scan_result.get("issues", [])),
        },
        "scan": scan_result,
        "quality": score_result,
    }

    if as_json:
        click.echo(json.dumps(report, indent=2))
    else:
        _render_audit(report)

    if not passed:
        if critical > 0:
            console.print(f"\n[red bold]✖ FAILED: {critical} critical security issue(s) found[/red bold]")
        if total_score < threshold:
            console.print(f"\n[red bold]✖ FAILED: Score {total_score}/100 is below threshold {threshold}[/red bold]")
        sys.exit(1)
    else:
        console.print(f"\n[green bold]✔ PASSED: {server} — score {total_score}/100, {len(scan_result.get('issues', []))} issue(s)[/green bold]")


def _render_audit(report: dict):
    """Render a comprehensive audit report."""
    server = report["server"]
    score = report["score"]
    issues = report["issues"]
    color = "green" if score >= 70 else "yellow" if score >= 40 else "red"

    console.print(Panel.fit(
        f"[bold]MCP Doctor Audit Report[/bold]\n"
        f"  Server:  [cyan]{server}[/cyan]\n"
        f"  Score:   [{color} bold]{score}/100[/{color} bold]\n"
        f"  Issues:  [red]{issues['critical']}[/red] critical, "
        f"[red]{issues['high']}[/red] high, "
        f"[yellow]{issues['medium']}[/yellow] medium, "
        f"[blue]{issues['low']}[/blue] low",
        title="🩺 Audit",
        border_style="cyan",
    ))

    # Security scan details
    console.print("\n[bold cyan]▸ Security Scan[/bold cyan]")
    _render_scan(report["scan"])

    # Quality breakdown
    console.print("\n[bold cyan]▸ Quality Score[/bold cyan]")
    _render_score(report["quality"])


@main.command(name="stats")
def stats_cmd():
    """Show registry statistics."""
    registry = get_registry()
    categories = {}
    for s in registry:
        cat = s.get("category", "other")
        categories[cat] = categories.get(cat, 0) + 1

    console.print(Panel.fit(
        f"[bold]MCP Doctor Registry[/bold]\n\n"
        f"  Total servers: [cyan]{len(registry)}[/cyan]\n"
        f"  Categories: [cyan]{len(categories)}[/cyan]\n"
        f"  Avg score: [cyan]{sum(s.get('score', 0) for s in registry) / max(len(registry), 1):.0f}[/cyan]\n\n"
        + "\n".join(f"  {cat:20s} [dim]{count} servers[/dim]" for cat, count in sorted(categories.items())),
        title="Registry Stats",
        border_style="cyan",
    ))


def _render_scan(result: dict):
    table = Table(show_header=True, header_style="bold")
    table.add_column("Severity", width=10)
    table.add_column("Issue")
    table.add_column("Details")

    for issue in result.get("issues", []):
        sev = issue.get("severity", "info")
        style = {"critical": "red bold", "high": "red", "medium": "yellow", "low": "blue", "info": "dim"}.get(sev, "")
        table.add_row(f"[{style}]{sev.upper()}[/{style}]", issue["title"], issue.get("detail", ""))

    if not result.get("issues"):
        table.add_row("[green]PASS[/green]", "No issues found", "")

    console.print(table)


def _render_score(result: dict):
    total = result.get("total", 0)
    color = "green" if total >= 70 else "yellow" if total >= 40 else "red"
    console.print(f"\n  Overall: [{color} bold]{total}/100[/{color} bold]\n")

    for cat, data in result.get("categories", {}).items():
        bar_len = int(data["score"] / 100 * 20)
        bar = "\u2588" * bar_len + "\u2591" * (20 - bar_len)
        console.print(f"  {cat:15s} [{bar}] {data['score']}/100  ({data.get('note', '')})")


def _render_table(servers: list):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan", max_width=40)
    table.add_column("Score", justify="right", width=6)
    table.add_column("Category", width=15)
    table.add_column("Stars", justify="right", width=8)
    table.add_column("Description", max_width=50)

    for s in servers:
        sc = s.get("score", 0)
        color = "green" if sc >= 70 else "yellow" if sc >= 40 else "red"
        table.add_row(
            s.get("name", "?"),
            f"[{color}]{sc}[/{color}]",
            s.get("category", ""),
            str(s.get("stars", "")),
            (s.get("description", "")[:48] + "...") if len(s.get("description", "")) > 50 else s.get("description", ""),
        )
    console.print(table)


if __name__ == "__main__":
    main()
