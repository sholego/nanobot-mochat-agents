<#
.SYNOPSIS
    Launch all 5 agents at once (each in its own window).

.EXAMPLE
    .\scripts\launch-all.ps1
#>

$agents = @("agent1-gemini", "agent2-deepseek", "agent3-qwen", "agent4-claude", "agent5-gpt")
$scriptDir = $PSScriptRoot

foreach ($agent in $agents) {
    $launchScript = Join-Path $scriptDir "launch-agent.ps1"
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$launchScript' -AgentName $agent"
    Write-Host "  🤖 $agent started" -ForegroundColor Green
}

Write-Host ""
Write-Host "All 5 agents launched! Check the new windows." -ForegroundColor Cyan
Write-Host "To stop all: close the 5 windows or press Ctrl+C in each." -ForegroundColor DarkGray
