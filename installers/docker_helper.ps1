<#
PowerShell helper to check for Docker and start the docker-compose stack included in the installer.
This script is intended to be run on Windows after files are installed. It will:
 - Check if 'docker' and 'docker compose' are available
 - If not present, open Docker Desktop download page for the user and exit
 - If present, run 'docker compose up -d' in the install directory
#>

param()

function Test-Command {
    param([string]$cmd)
    try {
        $proc = Start-Process -FilePath "powershell" -ArgumentList "-Command $cmd" -NoNewWindow -PassThru -Wait -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

Write-Host "Checking for Docker..."

try {
    $dockerVersion = & docker --version 2>$null
} catch {
    $dockerVersion = $null
}

if (-not $dockerVersion) {
    Write-Host "Docker CLI not found. Please install Docker Desktop from https://www.docker.com/get-started"
    Start-Process "https://www.docker.com/get-started"
    exit 1
}

Write-Host "Docker found: $dockerVersion"

# Use docker compose -f <path> up -d
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$composeFile = Join-Path $scriptDir '..\docker-compose.yml'
$composeFile = Resolve-Path $composeFile -ErrorAction SilentlyContinue
if (-not $composeFile) {
    Write-Host "Cannot find docker-compose.yml next to the installed tools. Make sure the installer copied the compose file into the install folder."
    exit 1
}

$composePath = $composeFile.Path
Write-Host "Starting docker compose stack from: $composePath"

try {
    Push-Location (Split-Path $composePath)
    docker compose -f "$(Split-Path $composePath -Leaf)" up -d
    Pop-Location
    Write-Host "Docker stack started (or already running)."
} catch {
    Write-Host "Failed to start Docker Compose stack: $_"
    exit 1
}

exit 0
