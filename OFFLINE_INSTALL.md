# Offline Installation Guide for Agriautonomous
# Complete guide for installing on PC without internet access

## Overview

This guide explains how to download all dependencies on a machine WITH internet access, then transfer them to your offline PC.

---

## Prerequisites

**Machine WITH Internet (Download Station):**
- Python 3.8+ installed
- pip package manager
- ~2-5GB free disk space (depending on what you install)
- USB drive or external storage

**Offline PC (Target Machine):**
- Python 3.8+ installed
- pip package manager
- The repository cloned locally

---

## Step 1: Download All Packages on Internet Machine

### Option A: Download All Requirements (Recommended)

On a machine with internet access:

```bash
# Create a directory for packages
mkdir agri-packages
cd agri-packages

# Download core packages
pip download -r ../requirements.txt -d ./packages

# Download development packages
pip download -r ../requirements-dev.txt -d ./packages

# Download radar packages
pip download -r ../requirements-radar.txt -d ./packages

# Download hardware packages
pip download -r ../requirements-hardware.txt -d ./packages

# Download AI/ML packages (optional - large!)
pip download -r ../requirements-ai.txt -d ./packages

# Download database packages
pip download -r ../requirements-database.txt -d ./packages

# Download cloud packages
pip download -r ../requirements-cloud.txt -d ./packages

# Download optional packages
pip download -r ../requirements-optional.txt -d ./packages
```

### Option B: Download Only Essentials (Smaller)

```bash
mkdir agri-packages-essential
cd agri-packages-essential

# Core + Radar only (minimal setup)
pip download -r ../requirements.txt -d ./packages
pip download -r ../requirements-radar.txt -d ./packages
```

### Option C: Download with Wheels (Faster Installation)

```bash
# Download with wheel format (pre-compiled, faster)
pip download --only-binary=:all: -r requirements.txt -d ./packages
```

---

## Step 2: Transfer to Offline PC

### Methods:

**USB Drive:**
```bash
# Copy packages folder to USB
cp -r agri-packages /media/usb/
# or on Windows: xcopy agri-packages\ E:\ /E /I
```

**External Hard Drive:**
```bash
cp -r agri-packages /mnt/external-drive/
```

**Network Transfer (if available):**
```bash
# From upload machine
python -m http.server 8000

# From download machine
wget -r http://[upload-machine-ip]:8000/agri-packages/
```

---

## Step 3: Install on Offline PC

### Step 3a: Setup Virtual Environment

```bash
cd Agriautonomous

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### Step 3b: Install from Downloaded Packages

```bash
# Install from local packages directory (replace PATH with actual path)
pip install --no-index --find-links /path/to/agri-packages/packages -r requirements.txt

# Or if you only downloaded core:
pip install --no-index --find-links ./agri-packages/packages -r requirements.txt
```

### Step 3c: Verify Installation

```bash
# Check if packages installed correctly
python -c "import PyQt5; print('PyQt5 OK')"
python -c "import folium; print('Folium OK')"
python -c "import numpy; print('NumPy OK')"

# Or run tests
pytest
```

---

## Option 4: Pre-Built Offline Package (Advanced)

### Create a Complete Offline Bundle

**On Internet Machine:**

```bash
# Create master directory
mkdir Agriautonomus-Offline
cd Agriautonomus-Offline

# Copy repository
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus

# Download ALL dependencies
mkdir offline-packages
pip download -r requirements.txt -d ./offline-packages
pip download -r requirements-dev.txt -d ./offline-packages
pip download -r requirements-radar.txt -d ./offline-packages
pip download -r requirements-hardware.txt -d ./offline-packages
pip download -r requirements-database.txt -d ./offline-packages

# Create install script
cat > install-offline.sh << 'EOF'
#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install --no-index --find-links ./offline-packages -r requirements.txt
echo "Installation complete!"
EOF

chmod +x install-offline.sh

# For Windows
cat > install-offline.bat << 'EOF'
@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install --no-index --find-links ./offline-packages -r requirements.txt
echo Installation complete!
EOF

# Compress everything
tar -czf Agriautonomus-Offline.tar.gz ../Agriautonomus-Offline/
# or on Windows: use 7-Zip or WinRAR
```

**Transfer to Offline PC:**

```bash
# Extract
tar -xzf Agriautonomus-Offline.tar.gz
cd Agriautonomus-Offline/Agriautonomus

# Run install script
# Linux/macOS:
./install-offline.sh

# Windows:
install-offline.bat

# Run application
Agriautonomous
```

---

## Step 5: Manual Dependency Installation (If Needed)

If some packages fail to install, you can install manually:

```bash
# Navigate to packages directory
cd offline-packages

# Install specific wheel files
pip install --no-deps PyQt5-5.15.7-py3-none-win_amd64.whl
pip install --no-deps folium-0.14.0-py2.py3-none-any.whl
# ... continue for each package

# Then install from requirements
pip install -r requirements.txt --no-index --find-links .
```

---

## Troubleshooting Offline Installation

### Issue: "No matching distribution found"

**Solution:** Re-download the specific package with dependencies

```bash
# On internet machine, download specific package with all deps
pip download package-name --no-cache-dir -d ./packages
pip download package-name --no-binary :all: -d ./packages
```

### Issue: "Building wheel for X failed"

**Solution:** Use pre-built wheels only

```bash
pip install --only-binary=:all: -r requirements.txt --no-index --find-links ./packages
```

### Issue: Different Python versions

**Solution:** Download for specific Python version

```bash
# On internet machine
pip download -r requirements.txt -d ./packages --python-version 38
# for Python 3.10:
pip download -r requirements.txt -d ./packages --python-version 310
```

### Issue: Missing system dependencies

For packages like `opencv-python` that need system libraries:

**On Offline PC (Linux):**
```bash
# Pre-install system dependencies
sudo apt-get install libsm6 libxext6 libxrender-dev  # For OpenCV
sudo apt-get install python3-dev  # For building wheels
```

**On Offline PC (Windows):**
- Download Visual C++ redistributables separately
- Install from: https://support.microsoft.com/en-us/help/2977003

---

## Complete Offline Bundle Checklist

Before transferring, verify you have:

```
agri-packages/
├── packages/
│   ├── PyQt5-5.15.7-*.whl
│   ├── numpy-1.24.3-*.whl
│   ├── folium-0.14.0-*.whl
│   ├── opencv-python-4.8.0.76-*.whl
│   ├── [all other .whl and .tar.gz files]
│   └── ... (500+ files)
├── requirements.txt
├── requirements-radar.txt
├── requirements-hardware.txt
├── requirements-database.txt
└── install-offline.sh (or .bat for Windows)
```

---

## Quick Offline Installation (TL;DR)

**On Internet Machine:**
```bash
pip download -r requirements.txt -r requirements-radar.txt -d ./agri-packages
```

**Transfer to USB and move to Offline PC:**

```bash
cd Agriautonomous
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --no-index --find-links ../agri-packages -r requirements.txt
Agriautonomous
```

---

## For Live Radar Without Internet

Live Radar **requires internet for real-time weather data**. However, you can:

1. **Cache data when online** - Download weather data in advance
2. **Use offline maps** - Use local map tiles instead of online
3. **Disable radar** - Run all other features offline

Configure offline mode:

```python
# In config/radar.json
{
  "radar": {
    "enabled": false,
    "offline_mode": true,
    "use_cached_data": true
  }
}
```

---

## Storage Requirements

- **Minimal** (core only): ~300 MB
- **Standard** (with Radar): ~800 MB
- **Full** (with AI/ML): ~2-3 GB

Choose downloads accordingly!

---

**Total Time:** ~30-60 minutes depending on internet speed and package size.

Happy Offline Farming! 🌾
