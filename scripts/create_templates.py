"""
Create template config.json.example files for all agents.
Run this to generate example configs for GitHub distribution.
"""
from __future__ import annotations

import json
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"

AGENTS = [
    ("agent1-gemini", "google/gemini-2.5-pro",
     "You are Agent-GM, a scholarly and knowledgeable AI. You provide logical, data-driven insights and enjoy discussing a wide range of topics. Always respond in Japanese."),
    ("agent2-deepseek", "deepseek/deepseek-v4",
     "You are Agent-DS, a deep-thinking researcher. You always dig deeper, asking 'Is that really true?' and challenging assumptions constructively. Always respond in Japanese."),
    ("agent3-qwen", "qwen/qwen3.5-397b-a17b",
     "You are Agent-QW, an international mediator. You see things from multiple cultural perspectives and bridge different viewpoints. Always respond in Japanese."),
    ("agent4-claude", "anthropic/claude-sonnet-4.6",
     "You are Agent-CL, an empathetic counselor. You prioritize emotional intelligence, ethical considerations, and creating a comfortable atmosphere. Always respond in Japanese."),
    ("agent5-gpt", "openai/gpt-5.2",
     "You are Agent-GP, a creative thinker and mood maker. You suggest unconventional ideas and bring humor and imagination to conversations. Always respond in Japanese."),
]

TEMPLATE = {
    "providers": {
        "openrouter": {
            "apiKey": "YOUR_OPENROUTER_API_KEY"
        }
    },
    "agents": {
        "defaults": {
            "model": "",
            "systemPrompt": ""
        }
    },
    "channels": {
        "mochat": {
            "enabled": True,
            "baseUrl": "https://mochat.io",
            "socketUrl": "https://mochat.io",
            "socketPath": "/socket.io",
            "clawToken": "YOUR_CLAW_TOKEN",
            "agentUserId": "YOUR_AGENT_USER_ID",
            "sessions": ["*"],
            "panels": [],
            "replyDelayMode": "non-mention",
            "replyDelayMs": 30000
        }
    }
}


def main() -> None:
    for agent_dir, model, prompt in AGENTS:
        config = json.loads(json.dumps(TEMPLATE))
        config["agents"]["defaults"]["model"] = model
        config["agents"]["defaults"]["systemPrompt"] = prompt

        out_dir = AGENTS_DIR / agent_dir / "home" / ".nanobot"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "config.json.example"
        out_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8"
        )
        print(f"  ✓ {agent_dir}/config.json.example")

    print("\nDone! Users should copy config.json.example to config.json and fill in their keys.")


if __name__ == "__main__":
    main()
