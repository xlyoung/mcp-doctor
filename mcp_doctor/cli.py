"""MCP Doctor CLI — Scan, Score, Install MCP Servers."""
import sys
import click
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
    import json
    result = scan_server(server)
    if as_json:
        click.echo(json.dumps(result, indent=2))
    else:
        _render_scan(result)


@main.command()
@click.argument("server")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def score(server: str, as_json: bool):
    """Score an MCP server\u2019s quality (0-100)."""
    import json
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
def install(server: str):
    """Scan + score + install an MCP server."""
    console.print(f"\n[bold]Running pre-install checks for:[/bold] {server}\n")

    # Step 1: Scan
    console.print("[bold cyan]\u276f Security Scan[/bold cyan]")
    scan_result = scan_server(server)
    _render_scan(scan_result)

    if scan_result.get("critical", 0) > 0:
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
