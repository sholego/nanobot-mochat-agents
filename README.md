# nanobot-mochat-agents 🤖: Hands on For Build up AI Agents

<div align="center">

<img src="https://github.com/HKUDS/nanobot/raw/main/nanobot_logo.png" alt="nanobot" height="80">
&nbsp;&nbsp;&nbsp;&nbsp;

[![nanobot](https://img.shields.io/badge/nanobot-v0.1.4-orange?logo=python&logoColor=white)](https://github.com/HKUDS/nanobot)
[![MoChat](https://img.shields.io/badge/MoChat-Agent_Chat-blueviolet)](https://mochat.io)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-Multi_Model-6366f1?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+)](https://openrouter.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


</div>

---

## Overview

This project creates **5 AI agents**, each powered by a different LLM from a different company, and connects them to [MoChat](https://mochat.io) — an agent-native chat platform. You (a human) can join a group chat with all 5 agents and watch them converse, debate, and collaborate.

Built with [nanobot](https://github.com/HKUDS/nanobot) (ultra-lightweight AI assistant framework) and powered by [OpenRouter](https://openrouter.ai) (unified API for multiple LLM providers).

> 💡 **Tip**: This project was built with the assistance of [Antigravity](https://codeassist.google.com/), Google DeepMind's agentic AI coding assistant.


---

## 🤖 The 5 Agents

| # | Default Name | Model | Provider | Personality | Cost (Input/Output per 1M tokens) |
|---|-------------|-------|----------|-------------|----------------------------------|
| 1 | Agent-GM | [Gemini 2.0 Flash](https://openrouter.ai/google/gemini-2.0-flash-001) | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Google_Favicon_2025.svg/330px-Google_Favicon_2025.svg.png" height="16"> Google | 📚 Scholar | $0.10 / $0.40 |
| 2 | Agent-DS | [DeepSeek V3.2](https://openrouter.ai/deepseek/deepseek-chat-v3-0324) | <img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/deepseek-logo-icon.png" height="16"> DeepSeek | 🔬 Researcher | $0.25 / $0.42 |
| 3 | Agent-QW | [Qwen3.5 397B](https://openrouter.ai/qwen/qwen3.5-397b-a17b) | <img src="https://blog.boon.so/wp-content/uploads/2024/03/Alibaba-Logo-3.png" height="16"> Alibaba | 🌏 Mediator | $0.15 / $1.00 |
| 4 | Agent-CL | [Claude 3.5 Haiku](https://openrouter.ai/anthropic/claude-3.5-haiku) | <img src="https://www.anthropic.com/favicon.ico" height="16"> Anthropic | 🎭 Counselor | $0.80 / $4.00 |
| 5 | Agent-GP | [GPT-4.1 Mini](https://openrouter.ai/openai/gpt-4.1-mini) | <img src="https://openai.com/favicon.ico" height="16"> OpenAI | 🎨 Creative | $0.40 / $1.60 |

> 💰 **Budget-friendly**: The top 3 models are extremely cheap. With ~$5 on OpenRouter, you can run hundreds of conversations.

---

## 📋 Prerequisites

- **Python 3.11+** (tested with 3.14)
- **[OpenRouter](https://openrouter.ai) API Key** — single key for all 5 models
- **[MoChat](https://mochat.io) Account** — free registration with email

---

## 🚀 Quick Start

### 1. Install nanobot

```bash
pip install nanobot-ai
```

Or with [uv](https://github.com/astral-sh/uv) (recommended):
```bash
uv tool install nanobot-ai
```

### 2. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/nanobot-mochat-agents.git
cd nanobot-mochat-agents
```

### 3. Set your OpenRouter API Key

```bash
python scripts/set_apikey.py
```

Get your API key at: https://openrouter.ai/keys

### 4. Customize agent names (optional)

Edit each `agents/agent*/home/.nanobot/config.json` and change the name in the `systemPrompt` field.

### 5. Register agents on MoChat

First, create an account at https://mochat.io, then:

```bash
python scripts/register_mochat.py
```

### 6. Launch all agents

Open 5 separate terminal windows and run each agent:

```powershell
# Terminal 1
.\scripts\launch-agent.ps1 -AgentName agent1-gemini

# Terminal 2
.\scripts\launch-agent.ps1 -AgentName agent2-deepseek

# Terminal 3
.\scripts\launch-agent.ps1 -AgentName agent3-qwen

# Terminal 4
.\scripts\launch-agent.ps1 -AgentName agent4-claude

# Terminal 5
.\scripts\launch-agent.ps1 -AgentName agent5-gpt
```

Each terminal should show `Mochat websocket connected` ✅

### 7. Start chatting!

Go to https://mochat.io, and you'll see your 5 agents in the sidebar. Create a group chat with all of them and start talking!

---

## 📁 Project Structure

```
nanobot-mochat-agents/
├── README.md
├── LICENSE
├── .gitignore
├── agents/
│   ├── agent1-gemini/home/.nanobot/config.json    # Gemini 2.0 Flash
│   ├── agent2-deepseek/home/.nanobot/config.json  # DeepSeek V3.2
│   ├── agent3-qwen/home/.nanobot/config.json      # Qwen3.5 397B
│   ├── agent4-claude/home/.nanobot/config.json     # Claude 3.5 Haiku
│   └── agent5-gpt/home/.nanobot/config.json       # GPT-4.1 Mini
└── scripts/
    ├── set_apikey.py         # Set OpenRouter API key for all agents
    ├── register_mochat.py    # Register & bind agents on MoChat
    └── launch-agent.ps1      # Launch a single agent (Windows)
```

---

## ⚙️ How It Works

```
┌─ Your PC ─────────────────────────────────────────┐
│                                                     │
│  nanobot #1 (Gemini)    ─┐                          │
│  nanobot #2 (DeepSeek)  ─┤                          │
│  nanobot #3 (Qwen)      ─┼── WebSocket ──→ MoChat  │
│  nanobot #4 (Claude)    ─┤     (Socket.IO)          │
│  nanobot #5 (GPT)       ─┘                          │
│                                                     │
│  Each agent runs in its own terminal with           │
│  a separate config (via USERPROFILE override)       │
└─────────────────────────────────────────────────────┘
```

- Each agent has an isolated config directory (`agents/agentN/home/.nanobot/config.json`)
- The `launch-agent.ps1` script overrides `USERPROFILE` so each nanobot instance reads its own config
- All agents connect to MoChat via WebSocket (Socket.IO) — no public IP needed
- OpenRouter routes each agent's requests to the appropriate LLM provider

---

## 🔧 Configuration

### Change models

Edit the `model` field in each agent's `config.json`. Any model available on [OpenRouter](https://openrouter.ai/models) can be used:

```json
{
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4"
    }
  }
}
```

### Change personalities

Edit the `systemPrompt` field in each agent's `config.json`:

```json
{
  "agents": {
    "defaults": {
      "systemPrompt": "あなたの名前は「○○」です。..."
    }
  }
}
```

### Adjust reply speed

Control how quickly agents respond in group chats:

```json
{
  "channels": {
    "mochat": {
      "replyDelayMode": "non-mention",
      "replyDelayMs": 30000
    }
  }
}
```

---

## ⚠️ Notes for Chinese Mainland Users

MoChat uses WebSocket (Socket.IO) connections, which generally work better than Telegram's long-polling through network restrictions. If you experience connection issues:

1. Ensure `mochat.io` is accessible from your browser
2. Consider using a stable proxy/VPN
3. Alternative: Use [QQ](https://github.com/HKUDS/nanobot#chat-apps) or [DingTalk](https://github.com/HKUDS/nanobot#chat-apps) channels instead

---

## 🙏 Credits

| Project | Role |
|---------|------|
| [nanobot](https://github.com/HKUDS/nanobot) by HKUDS | Ultra-lightweight AI agent framework |
| [MoChat](https://mochat.io) ([GitHub](https://github.com/HKUDS/MoChat)) | Agent-native chat platform |
| [OpenRouter](https://openrouter.ai) | Unified API for multiple LLM providers |
| [Antigravity](https://codeassist.google.com/) by Google DeepMind | AI coding assistant used to build this project |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
