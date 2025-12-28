"""CLI entry point for the Scoring Evaluator agent."""

import json
import click
from rich.console import Console
from .agent import run_agent
from .memory import SessionMemory

console = Console()

@click.group()
def cli():
    """Ideation Agent: Scoring Evaluator - Scoring (problem & solution phases)."""
    pass

@cli.command()
@click.option("--session-id", required=True, help="Session ID for Mem0 context")
@click.option("--problem", default=None, help="Problem statement (optional)")
@click.option("--output-json", is_flag=True, help="Output results as JSON")
def run(session_id: str, problem: str | None, output_json: bool):
    """Run the agent for a given session."""
    memory = SessionMemory(session_id)

    if not problem:
        session = memory.get_session()
        if not session:
            console.print(f"[red]Error: No session found for {session_id}[/red]")
            raise SystemExit(1)
        problem = session.get("problem")

    console.print(f"[blue]Running scoring-evaluator agent for session: {session_id}[/blue]")
    result = run_agent(session_id, problem)
    memory.update_phase("scoring_evaluator", "complete", result)

    if output_json:
        print(json.dumps(result, indent=2))
    else:
        console.print("[green]Scoring Evaluator agent completed successfully[/green]")

if __name__ == "__main__":
    cli()
