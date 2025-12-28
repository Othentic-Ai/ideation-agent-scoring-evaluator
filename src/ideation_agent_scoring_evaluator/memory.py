"""Mem0 integration for session-based context sharing across agents."""

import json
import os
from datetime import datetime
from typing import Optional

from mem0 import MemoryClient


class SessionMemory:
    """Memory service for session-based context sharing."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.user_id = f"ideation_session_{session_id}"
        self._client = None

    @property
    def client(self) -> MemoryClient:
        if self._client is None:
            api_key = os.getenv("MEM0_API_KEY")
            if not api_key:
                raise ValueError("MEM0_API_KEY environment variable is required")
            self._client = MemoryClient(api_key=api_key)
        return self._client

    def get_session(self) -> Optional[dict]:
        try:
            results = self.client.search(
                f"session {self.session_id}",
                user_id=self.user_id,
                limit=1,
                filters={"metadata": {"type": "session"}}
            )
            if results.get("results"):
                memory = results["results"][0].get("memory", "")
                try:
                    return json.loads(memory)
                except json.JSONDecodeError:
                    return {"raw": memory}
            return None
        except Exception as e:
            print(f"[mem0] Warning: Failed to get session: {e}")
            return None

    def update_phase(self, phase: str, status: str, output: dict) -> bool:
        memory_text = f"""
Phase Update: {phase}
Session: {self.session_id}
Status: {status}
Updated: {datetime.now().isoformat()}

Output:
{json.dumps(output, indent=2)[:3000]}
"""
        try:
            self.client.add(
                memory_text,
                user_id=self.user_id,
                metadata={
                    "type": "phase_output",
                    "session_id": self.session_id,
                    "phase": phase,
                    "status": status,
                    "timestamp": datetime.now().isoformat()
                }
            )
            return True
        except Exception as e:
            print(f"[mem0] Warning: Failed to update phase: {e}")
            return False
