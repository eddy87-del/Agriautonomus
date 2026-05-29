#!/bin/bash
# Linux installation script

set -e

echo "====================================="
echo "Agriautonomous Installation - Linux"
echo "====================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "This script requires sudo privileges"
  exit 1
fi

echo "Installing system dependencies..."
apt-get update
apt-get install -y \
  python3.9 \
  python3-pip \
  python3-dev \
  libqt5gui5 \
  libqt5core5a \
  libqt5widgets5

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Building application..."
pip3 install --upgrade setuptools wheel
python3 setup.py bdist_wheel

echo "Installing application..."
pip3 install dist/agriautonomous-2.0.0-py3-none-any.whl

echo "Creating desktop entry..."
cat > /usr/share/applications/agriautonomous.desktop << EOF
[Desktop Entry]
Type=Application
Name=Agriautonomous
Comment=Autonomous Rice Farm Control System
Exec=Agriautonomous
Icon=agriautonomous
Categories=Utility;
Terminal=false
EOF

echo "Installation complete!"
echo "Run 'Agriautonomous' to start the application"
