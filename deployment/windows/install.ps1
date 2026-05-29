# Windows Installation Script
# Run as Administrator in PowerShell

Write-Host "Installing Agriautonomous on Windows"

# Install Chocolatey packages
choco install python postgresql mosquitto git -y

# Clone repository
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Python packages
pip install -r requirements.txt

# Setup database
psql -U postgres < database/schema.sql

Write-Host "Installation complete!"
