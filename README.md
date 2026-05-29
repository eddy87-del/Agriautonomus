# Agriautonomous - Desktop Installation System

**Version:** 2.0.0  
**Type:** Standalone Desktop Application  
**Status:** Production Ready

## Overview

Agriautonomous is a comprehensive autonomous farming system delivered as a **standalone desktop application** with native installers for Windows, Linux, and macOS.

## Features

- ✅ **Native Desktop GUI** - PyQt5-based control center
- ✅ **Command-line Tools** - Advanced CLI management
- ✅ **Offline-first** - Works without internet
- ✅ **Hardware Integration** - Direct device drivers
- ✅ **System Services** - Auto-start capabilities
- ✅ **One-click Installation** - Easy setup for farmers

## Installation

### Windows
```bash
Agriautonomous-2.0.0-Setup.exe
```

### Linux
```bash
sudo dpkg -i agriautonomous_2.0.0_amd64.deb
# or
sudo rpm -i agriautonomous-2.0.0-1.x86_64.rpm
```

### macOS
```bash
Agriautonomous-2.0.0.dmg
```

## Quick Start

1. **Install** using the installer for your OS
2. **Launch** Agriautonomous from Applications/Programs menu
3. **Configure** your farm and devices
4. **Start** operating autonomous systems

## System Requirements

- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 10GB free space
- **OS:** Windows 10+, Ubuntu 20.04+, macOS 10.14+
- **Network:** Optional (works offline)

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [User Manual](docs/USER_MANUAL.md)
- [Configuration Guide](docs/CONFIGURATION.md)
- [Developer Guide](docs/DEVELOPER.md)

## Project Structure

```
Agriautonomous/
├── src/
│   ├── gui/                 # PyQt5 Desktop GUI
│   ├── cli/                 # Command-line tools
│   ├── core/                # Core business logic
│   ├── hardware/            # Device drivers
│   ├── ai/                  # AI models
│   ├── database/            # Local database
│   └── services/            # Background services
├── installers/              # Platform-specific installers
├── resources/               # Images, icons, configs
├── tests/                   # Unit and integration tests
├── docs/                    # Documentation
└── setup.py                 # Build configuration
```

## License

MIT License - See LICENSE file
