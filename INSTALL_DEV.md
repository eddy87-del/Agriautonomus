# Agriautonomous - Development Installation & Testing Guide

This guide will help you install and run **Agriautonomous** on your PC for development and testing, including **Live Radar** functionality.

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Git** installed
- **4GB+ RAM** (8GB recommended)
- **500MB+ free disk space**
- **Internet connection** (for initial setup and live radar data)

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

**For Live Radar Support** - Additional dependencies:
```bash
pip install requests folium pyproj python-dateutil
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

## Live Radar Integration

Agriautonomous includes **real-time weather radar** visualization for monitoring farm conditions.

### Enable Live Radar

**Via GUI:**
1. Launch the application: `Agriautonomous`
2. Navigate to **Tools** → **Live Radar**
3. Enter your farm coordinates (latitude, longitude)
4. Click **Start Radar** to begin monitoring

**Via CLI:**
```bash
agri radar --start --lat 37.7749 --lon -122.4194
agri radar --stop
agri radar --status
```

### Live Radar Features

✅ **Real-time Weather Data** - Live precipitation, wind, temperature  
✅ **Storm Tracking** - Detect and track incoming storms  
✅ **Satellite Imagery** - Cloud coverage and weather patterns  
✅ **Alerts** - Automatic notifications for severe weather  
✅ **Historical Data** - Review past weather events  
✅ **Export Reports** - Generate weather/radar reports  

### Testing Live Radar

```bash
# Test radar connection
agri radar --test

# Test with specific coordinates (Los Angeles example)
agri radar --test --lat 34.0522 --lon -118.2437

# Run radar test suite
pytest tests/test_radar.py -v

# Test radar with mock data (offline mode)
agri radar --test --mock
```

### Live Radar Configuration

Edit or create `config/radar.json`:

```json
{
  "radar": {
    "enabled": true,
    "update_interval": 300,
    "data_source": "weather_api",
    "cache_enabled": true,
    "cache_duration": 600,
    "alerts_enabled": true,
    "alert_threshold": {
      "wind_speed": 40,
      "precipitation": 50,
      "temperature_min": 0,
      "temperature_max": 45
    }
  }
}
```

### Live Radar API

If using programmatically:

```python
from agriautonomous.radar import RadarManager

# Initialize radar
radar = RadarManager(
    latitude=37.7749,
    longitude=-122.4194,
    update_interval=300
)

# Start monitoring
radar.start()

# Get current conditions
conditions = radar.get_current_conditions()
print(f"Temperature: {conditions['temperature']}°C")
print(f"Wind Speed: {conditions['wind_speed']} km/h")
print(f"Precipitation: {conditions['precipitation']} mm")

# Get alerts
alerts = radar.get_alerts()
for alert in alerts:
    print(f"ALERT: {alert['severity']} - {alert['message']}")

# Stop monitoring
radar.stop()
```

### Live Radar Data Sources

The system supports multiple weather data providers:

- **OpenWeatherMap** - Free & Pro tiers
- **WeatherAPI** - Real-time + historical
- **NOAA** - US Weather radar data
- **Local Sensors** - Integration with on-site equipment

Configure your preferred source in settings:

```bash
agri config --set weather.provider openweathermap
agri config --set weather.api_key YOUR_API_KEY_HERE
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

# Run radar-specific tests
pytest tests/test_radar.py -v

# Run with verbose output
pytest -v

# Run tests with live radar enabled
pytest tests/ -m radar
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

### Issue: Live Radar Not Loading
**Solution 1:** Check internet connection
```bash
ping google.com
```

**Solution 2:** Verify API credentials
```bash
agri config --get weather.api_key
```

**Solution 3:** Check firewall/proxy settings
```bash
agri radar --test --verbose
```

### Issue: Radar Data Not Updating
**Solution 1:** Check update interval (default: 5 minutes)
```bash
agri config --get radar.update_interval
```

**Solution 2:** Verify coordinates are correct
```bash
agri config --get farm.latitude
agri config --get farm.longitude
```

**Solution 3:** Restart radar service
```bash
agri radar --restart
```

---

## Project Structure

```
Agriautonomous/
├── src/
│   ├── agriautonomous/
│   │   ├── __init__.py
│   │   ├── gui/                 # PyQt5 Desktop GUI
│   │   │   └── radar_widget.py  # Live Radar UI
│   │   ├── cli/                 # Command-line tools
│   │   │   └── radar_cli.py     # Radar commands
│   │   ├── core/                # Core business logic
│   │   ├── hardware/            # Device drivers
│   │   ├── ai/                  # AI models
│   │   ├── database/            # Local database
│   │   ├── radar/               # Live Radar module
│   │   │   ├── manager.py       # Radar manager
│   │   │   ├── data_sources.py  # Weather API integrations
│   │   │   └── visualization.py # Radar visualization
│   │   └── services/            # Background services
├── tests/
│   ├── test_radar.py            # Radar tests
│   ├── test_gui.py
│   └── test_cli.py
├── config/
│   └── radar.json               # Radar configuration
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
| **Network** | Recommended (for radar) | High-speed internet |
| **Display** | 1024x768 | 1920x1080+ |

---

## Quick Start Commands

```bash
# Full setup from scratch with Live Radar
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install requests folium pyproj python-dateutil
pip install -e .

# Configure your farm location
agri config --set farm.name "My Test Farm"
agri config --set farm.latitude 37.7749
agri config --set farm.longitude -122.4194

# Test radar connection
agri radar --test

# Run the application with Live Radar
Agriautonomous

# Run all tests including radar
pytest -v
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
- See [RADAR_GUIDE.md](docs/RADAR_GUIDE.md) for detailed radar documentation

---

## Support

For issues or questions:
- Create a [GitHub Issue](https://github.com/eddy87-del/Agriautonomus/issues)
- Check existing documentation in `docs/` folder
- Contact: spark@agriautonomous.com

---

**Happy Farming with Live Radar! 🌾📡**
