#!/bin/bash
# Linux Installation Script

echo "Installing Agriautonomous on Linux"

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3.9 python3-pip postgresql mosquitto git

# Clone repository
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Setup database
sudo -u postgres psql < database/schema.sql

echo "Installation complete!"
