<#
.SYNOPSIS
    Launch a single nanobot agent with its own isolated config.

.DESCRIPTION
    Overrides USERPROFILE/HOMEDRIVE/HOMEPATH so that nanobot reads the
    agent-specific config.json instead of the global ~/.nanobot/config.json.

.PARAMETER AgentName
    Agent directory name (e.g., agent1-gemini, agent2-deepseek).

.EXAMPLE
    .\scripts\launch-agent.ps1 -AgentName agent1-gemini
#>
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet(
        "agent1-gemini",
        "agent2-deepseek",
        "agent3-qwen",
        "agent4-claude",
        "agent5-gpt"
    )]
    [string]$AgentName
)

$agentHome = Join-Path $PSScriptRoot (Join-Path "..\agents" (Join-Path $AgentName "home"))
$agentHome = (Resolve-Path $agentHome).Path

if (-not (Test-Path (Join-Path $agentHome ".nanobot\config.json"))) {
    Write-Host "Error: config.json not found at $agentHome\.nanobot\config.json" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "  Agent:  $AgentName" -ForegroundColor Cyan
Write-Host "  Config: $agentHome\.nanobot\config.json" -ForegroundColor DarkGray
Write-Host ""

# Override home directory for this process so nanobot reads agent-specific config
$env:USERPROFILE = $agentHome
$env:HOME = $agentHome
$env:HOMEDRIVE = Split-Path $agentHome -Qualifier
$env:HOMEPATH = Split-Path $agentHome -NoQualifier
$env:PYTHONUTF8 = "1"

# Find nanobot executable
$nanobot = Get-Command nanobot -ErrorAction SilentlyContinue
if ($nanobot) {
    & $nanobot.Source gateway
}
else {
    # Fallback: try common Python 3.11+ locations
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA "Python\pythoncore-3.14-64\Scripts\nanobot.exe"),
        (Join-Path $env:LOCALAPPDATA "Python\pythoncore-3.13-64\Scripts\nanobot.exe"),
        (Join-Path $env:LOCALAPPDATA "Python\Python314\Scripts\nanobot.exe"),
        (Join-Path $env:LOCALAPPDATA "Python\Python313\Scripts\nanobot.exe"),
        (Join-Path $env:LOCALAPPDATA "Python\Python312\Scripts\nanobot.exe"),
        (Join-Path $env:LOCALAPPDATA "Python\Python311\Scripts\nanobot.exe")
    )
    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) {
            & $candidate gateway
            return
        }
    }
    Write-Host "Error: nanobot not found. Install with: pip install nanobot-ai" -ForegroundColor Red
    exit 1
}
