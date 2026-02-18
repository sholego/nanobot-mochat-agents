"""
Register agents on MoChat and bind them to your account.

Usage:
    python scripts/register_mochat.py

This script will:
    1. Register each agent on MoChat (selfRegister API)
    2. Optionally bind them to your email (so they appear in your MoChat account)
    3. Update each agent's config.json with the received credentials
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

MOCHAT_API = "https://mochat.io/api/claw/agents"
AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"

# Agent directory name -> display name
AGENTS: list[tuple[str, str]] = [
    ("agent1-gemini", "Agent-GM"),
    ("agent2-deepseek", "Agent-DS"),
    ("agent3-qwen", "Agent-QW"),
    ("agent4-claude", "Agent-CL"),
    ("agent5-gpt", "Agent-GP"),
]


def _post_json(url: str, payload: dict[str, Any], token: str | None = None) -> dict[str, Any]:
    """Send a POST request with JSON body and return parsed response."""
    data = json.dumps(payload).encode("utf-8")
    headers: dict[str, str] = {"Content-Type": "application/json"}
    if token:
        headers["X-Claw-Token"] = token
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        result: dict[str, Any] = json.loads(resp.read().decode("utf-8"))
        return result


def register_agent(name: str) -> dict[str, Any]:
    """Register a new agent on MoChat."""
    return _post_json(f"{MOCHAT_API}/selfRegister", {"name": name})


def bind_agent(token: str, email: str) -> dict[str, Any]:
    """Bind an agent to an owner by email."""
    return _post_json(
        f"{MOCHAT_API}/bind",
        {"email": email, "greeting_msg": f"Hello! I'm your AI agent."},
        token=token,
    )


def update_config(agent_dir: str, token: str, user_id: str) -> None:
    """Write MoChat credentials into the agent's config.json."""
    config_path = AGENTS_DIR / agent_dir / "home" / ".nanobot" / "config.json"
    with open(config_path, encoding="utf-8") as f:
        config: dict[str, Any] = json.load(f)
    config["channels"]["mochat"]["clawToken"] = token
    config["channels"]["mochat"]["agentUserId"] = user_id
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=True)


def main() -> None:
    email = input("MoChat email (press Enter to skip bind): ").strip()

    if email:
        print(f"\nOwner email: {email}")
    else:
        print("\n※ No email — bind step will be skipped")
    print("=" * 50)

    ok_count = 0
    for agent_dir, agent_name in AGENTS:
        print(f"\n🤖 Registering {agent_name}...")
        try:
            reg = register_agent(agent_name)
            data = reg.get("data", reg)
            token = data.get("token", "")
            user_id = data.get("botUserId", "")
            print(f"   ✓ Registered (ID: {user_id})")

            if email:
                try:
                    bind_agent(token, email)
                    print("   ✓ Bound to owner")
                except Exception as e:
                    print(f"   ⚠ Bind failed (can retry later): {e}")

            update_config(agent_dir, token, user_id)
            print("   ✓ config.json updated")
            ok_count += 1
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            print(f"   ✗ HTTP {e.code}: {body[:200]}")
        except Exception as e:
            print(f"   ✗ Error: {e}")

    print(f"\n{'=' * 50}")
    print(f"{ok_count}/{len(AGENTS)} agents registered successfully!")
    if ok_count > 0:
        print("Next: Launch agents with scripts/launch-agent.ps1")


if __name__ == "__main__":
    main()
