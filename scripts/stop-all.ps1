<#
.SYNOPSIS
    Stop all running nanobot gateway processes.

.EXAMPLE
    .\scripts\stop-all.ps1
#>

$procs = Get-Process -Name "nanobot" -ErrorAction SilentlyContinue
if ($procs) {
    $procs | Stop-Process -Force
    Write-Host "  Stopped $($procs.Count) nanobot process(es)." -ForegroundColor Yellow
}
else {
    Write-Host "  No nanobot processes found." -ForegroundColor DarkGray
}
