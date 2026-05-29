#!/bin/bash
# macOS installation script

echo "====================================="
echo "Agriautonomous Installation - macOS"
echo "====================================="

echo "Installing system dependencies..."
brew install python@3.9 qt5

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Building application..."
pip3 install --upgrade setuptools wheel py2app
python3 setup.py py2app

echo "Creating DMG..."
# Create DMG from the app bundle
hdiutil create -volname Agriautonomous \
  -srcfolder dist/Agriautonomous.app \
  -ov -format UDZO Agriautonomous-2.0.0.dmg

echo "Installation complete!"
echo "Run 'dist/Agriautonomous.app/Contents/MacOS/Agriautonomous' to start"
