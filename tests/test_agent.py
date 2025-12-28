"""Tests for the Scoring Evaluator agent."""

from pathlib import Path

def test_system_prompt_exists():
    prompt_path = Path(__file__).parent.parent / "src" / "ideation_agent_scoring_evaluator" / "prompts" / "system.md"
    assert prompt_path.exists()

def test_cli_import():
    from ideation_agent_scoring_evaluator.main import cli
    assert cli is not None
