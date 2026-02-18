"""
Set OpenRouter API key for all agent config files.

Usage:
    python scripts/set_apikey.py
"""
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    key = input("Enter your OpenRouter API key: ").strip()
    if not key:
        print("Error: API key is empty")
        return

    agents_dir = Path(__file__).resolve().parent.parent / "agents"
    configs = sorted(agents_dir.rglob("config.json"))

    if not configs:
        print("Error: No config.json files found")
        return

    for config_path in configs:
        with open(config_path, encoding="utf-8") as f:
            data = json.load(f)
        data["providers"]["openrouter"]["apiKey"] = key
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=True)
        agent_name = config_path.parts[-4]
        print(f"  ✓ {agent_name}")

    print(f"\nDone! Updated {len(configs)} config(s).")


if __name__ == "__main__":
    main()
