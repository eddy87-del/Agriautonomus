"""Installation Guide"""

# Agriautonomous Installation Guide

## System Requirements

- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 10GB free space
- **OS:** Windows 10+, Ubuntu 20.04+, macOS 10.14+
- **Python:** 3.8+ (included in installer)

## Windows Installation

### Method 1: Executable Installer (Recommended)

1. Download `Agriautonomous-2.0.0-Setup.exe`
2. Double-click to run installer
3. Follow installation wizard
4. Click "Launch" after installation

### Method 2: Manual Installation

1. Install Python 3.9+ from python.org
2. Open PowerShell as Administrator
3. Run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\installers\windows\install.ps1
   ```

## Linux Installation

### Ubuntu/Debian

1. Open Terminal
2. Make script executable:
   ```bash
   chmod +x installers/linux/install.sh
   ```
3. Run installer:
   ```bash
   sudo ./installers/linux/install.sh
   ```
4. Launch from Applications menu

### Alternative: DEB Package

```bash
sudo dpkg -i agriautonomous_2.0.0_amd64.deb
agriautonomous
```

## macOS Installation

### Method 1: DMG (Recommended)

1. Download `Agriautonomous-2.0.0.dmg`
2. Double-click DMG file
3. Drag Agriautonomous to Applications folder
4. Launch from Applications

### Method 2: Manual Installation

1. Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Open Terminal
3. Make script executable:
   ```bash
   chmod +x installers/macos/install.sh
   ```
4. Run installer:
   ```bash
   ./installers/macos/install.sh
   ```

## Post-Installation

### First Launch

1. Launch Agriautonomous from your applications menu
2. Complete initial setup wizard
3. Configure farm parameters
4. Register your hardware devices
5. Start operating autonomous systems

### Configuration

Configuration files are stored in:
- **Windows:** `C:\Users\YourUsername\.agriautonomous\config\`
- **Linux:** `~/.agriautonomous/config/`
- **macOS:** `~/.agriautonomous/config/`

### Data Storage

Application data is stored in:
- **Missions:** `~/.agriautonomous/missions/`
- **Logs:** `~/.agriautonomous/logs/`
- **Database:** `~/.agriautonomous/data/`

## Uninstallation

### Windows
1. Go to Settings → Apps → Apps & features
2. Search for "Agriautonomous"
3. Click Uninstall

### Linux
```bash
sudo apt-get remove agriautonomous
```

### macOS
1. Open Finder
2. Go to Applications
3. Drag Agriautonomous to Trash

## Troubleshooting

### Application Won't Start

**Solution:**
```bash
# Check logs
cat ~/.agriautonomous/logs/agriautonomous.log

# Reinstall
pip install --force-reinstall agriautonomous
```

### Hardware Not Detected

**Solution:**
1. Check serial port: `agri hardware --scan`
2. Verify cable connections
3. Install drivers if needed
4. Update device firmware

### Database Errors

**Solution:**
```bash
# Reset database
agri database --reset

# Backup and restore
agri database --backup
agri database --restore backup.json
```

## Support

For issues or questions:
- GitHub Issues: https://github.com/eddy87-del/Agriautonomus/issues
- Email: support@agriautonomous.com
- Documentation: https://agriautonomous.readthedocs.io
