# Ideation Agent: Scoring Evaluator

This is a specialized Claude Code agent for Scoring (problem & solution phases).

## What This Agent Does

When invoked, this agent:
1. Reads the problem/topic from Mem0 using the provided session-id
2. Executes its specialized analysis
3. Writes results back to Mem0 for the orchestrator to retrieve

## How to Run

```bash
pip install -e .
ideation-agent-scoring-evaluator run --session-id <session-id>
```

## Environment Variables

- `ANTHROPIC_API_KEY`: Required for Claude API access
- `MEM0_API_KEY`: Required for Mem0 cloud storage

## Agent Behavior

Read the system prompt at `src/ideation_agent_scoring_evaluator/prompts/system.md` for the agent's detailed behavior.
