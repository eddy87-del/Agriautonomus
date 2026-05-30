# Agriautonomous - Development Installation & Testing Guide

This guide will help you install and run **Agriautonomous** on your PC for development and testing.

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Git** installed
- **4GB+ RAM** (8GB recommended)
- **500MB+ free disk space**

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus
```

---

## Step 2: Create a Virtual Environment (Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

---

## Step 3: Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Optional** - For development and testing:
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy
```

---

## Step 4: Install in Development Mode

```bash
pip install -e .
```

This installs the package in editable mode, so changes to the code are immediately reflected.

---

## Step 5: Verify Installation

Check that the CLI is accessible:
```bash
agriautonomous --version
agri --help
```

---

## Running the Application

### Launch the Desktop GUI

**Windows:**
```bash
python -m agriautonomous.gui
```

**macOS/Linux:**
```bash
python -m agriautonomous.gui
```

Or simply:
```bash
Agriautonomous
```

### Using the CLI

```bash
agri --help
agri status
agri config --list
agri farm --create "My Farm"
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src

# Run specific test file
pytest tests/test_gui.py

# Run with verbose output
pytest -v
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'PyQt5'`
**Solution:** Reinstall dependencies
```bash
pip install --force-reinstall -r requirements.txt
```

### Issue: Virtual Environment Not Activating
**Windows:**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Issue: Permission Denied (macOS/Linux)
```bash
chmod +x setup.py
sudo pip install -e .
```

### Issue: Python Version Mismatch
Ensure Python 3.8+:
```bash
python --version
# or
python3 --version
```

---

## Project Structure

```
Agriautonomous/
├── src/
│   ├── agriautonomous/
│   │   ├── __init__.py
│   │   ├── gui/                 # PyQt5 Desktop GUI
│   │   ├── cli/                 # Command-line tools
│   │   ├── core/                # Core business logic
│   │   ├── hardware/            # Device drivers
│   │   ├── ai/                  # AI models
│   │   ├── database/            # Local database
│   │   └── services/            # Background services
├── tests/                       # Unit and integration tests
├── resources/                   # Images, icons, configs
├── docs/                        # Documentation
├── requirements.txt             # Dependencies
├── setup.py                     # Installation config
└── README.md                    # Main documentation
```

---

## Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/my-feature
```

### 2. Make Changes & Test
```bash
# Run tests
pytest

# Check code quality
flake8 src/
black src/
```

### 3. Commit Changes
```bash
git add .
git commit -m "Add new feature"
```

### 4. Push & Create Pull Request
```bash
git push origin feature/my-feature
```

---

## System Requirements (PC)

| Requirement | Minimum | Recommended |
|---|---|---|
| **CPU** | 2-core 2.0GHz | 4-core 2.5GHz+ |
| **RAM** | 4GB | 8GB |
| **Storage** | 500MB | 2GB |
| **OS** | Windows 10, Ubuntu 20.04, macOS 10.14+ | Latest version |
| **Network** | Optional | N/A |

---

## Quick Start Commands

```bash
# Full setup from scratch
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .

# Run the application
Agriautonomous

# Run tests
pytest
```

---

## Uninstalling

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment folder
rm -rf venv  # or delete folder on Windows

# Uninstall package
pip uninstall agriautonomous
```

---

## Next Steps

- Read [USER_MANUAL.md](docs/USER_MANUAL.md) for feature documentation
- Check [CONFIGURATION.md](docs/CONFIGURATION.md) for setup options
- Review [DEVELOPER.md](docs/DEVELOPER.md) for architecture details

---

## Support

For issues or questions:
- Create a [GitHub Issue](https://github.com/eddy87-del/Agriautonomus/issues)
- Check existing documentation in `docs/` folder
- Contact: spark@agriautonomous.com

---

**Happy Farming! 🌾**
