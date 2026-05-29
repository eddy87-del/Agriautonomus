# PowerShell installation script for Windows
# Run as Administrator

Write-Host "====================================="
Write-Host "Agriautonomous Installation - Windows"
Write-Host "====================================="

if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    Write-Host "This script requires administrator privileges"
    exit 1
}

# Install Python packages
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# Build application
Write-Host "Building application..."
python setup.py bdist_wheel

# Install application
Write-Host "Installing application..."
pip install dist/agriautonomous-2.0.0-py3-none-any.whl

# Create Start Menu shortcut
Write-Host "Creating Start Menu shortcut..."
$TargetPath = "C:\\Program Files\\Python39\\Scripts\\Agriautonomous.exe"
$ShortcutPath = "$([Environment]::GetFolderPath('CommonPrograms'))\\Agriautonomous.lnk"
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.WorkingDirectory = "$env:USERPROFILE"
$Shortcut.Save()

Write-Host "Installation complete!"
Write-Host "Find 'Agriautonomous' in your Start Menu"
