# Local Deployment Guide for Agriautonomous
# Complete guide for deploying on local PC/network without internet

---

## Overview

Local deployment allows you to run Agriautonomous as:
- **Desktop Application** - Native GUI on your PC
- **Local Web Server** - Access via browser on same network
- **Background Service** - Auto-start on PC boot
- **LAN Service** - Share across multiple devices on your network

---

## Option 1: Desktop Application (Simplest)

### Step 1: Install

```bash
# Clone repository
git clone https://github.com/eddy87-del/Agriautonomus.git
cd Agriautonomus

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Step 2: Run Application

```bash
# Launch GUI application
Agriautonomous

# Or with Python directly
python -m agriautonomous.gui
```

### Step 3: Verify It Works

- Desktop window should open
- Click Tools → Live Radar
- Enter your location coordinates
- Test radar functionality

---

## Option 2: Local Web Server (Browser Access)

### Step 1: Create Web Server Script

Create file: `src/agriautonomous/web_server.py`

```python
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
CORS(app)

# Configuration
CONFIG_PATH = os.path.expanduser('~/.agriautonomous/config.json')

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html')

@app.route('/api/status')
def status():
    """System status endpoint"""
    return jsonify({
        'status': 'running',
        'version': '2.0.0',
        'mode': 'local',
        'radar_enabled': True
    })

@app.route('/api/farm')
def farm_data():
    """Get farm configuration"""
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        return jsonify(config.get('farm', {}))
    except:
        return jsonify({'latitude': 0, 'longitude': 0, 'name': 'My Farm'})

@app.route('/api/radar/current')
def radar_current():
    """Get current radar/weather data"""
    return jsonify({
        'temperature': 25.5,
        'wind_speed': 12,
        'precipitation': 0,
        'humidity': 65,
        'last_update': '2026-06-04T12:00:00Z'
    })

@app.route('/api/radar/forecast')
def radar_forecast():
    """Get weather forecast"""
    return jsonify({
        'forecast': [
            {'time': '12:00', 'temp': 25, 'rain': 0},
            {'time': '15:00', 'temp': 26, 'rain': 10},
            {'time': '18:00', 'temp': 24, 'rain': 20}
        ]
    })

@app.route('/api/devices')
def devices():
    """List connected devices"""
    return jsonify({
        'devices': [
            {'id': 'device-1', 'name': 'Sensor 1', 'status': 'online', 'type': 'temperature'},
            {'id': 'device-2', 'name': 'Sprinkler', 'status': 'online', 'type': 'actuator'}
        ]
    })

@app.route('/api/device/<device_id>/control', methods=['POST'])
def control_device(device_id):
    """Control device"""
    data = request.json
    return jsonify({'success': True, 'message': f'Device {device_id} controlled'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    print("Starting Agriautonomous Web Server...")
    print("Access at: http://localhost:5000")
    print("Or from network: http://<your-ip>:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Step 2: Create Web Interface

Create file: `src/agriautonomous/web/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agriautonomous - Local Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav class="navbar">
        <h1>🌾 Agriautonomous Local Control</h1>
        <span id="status" class="status">● Online</span>
    </nav>

    <div class="container">
        <div class="dashboard">
            <!-- Status Card -->
            <div class="card">
                <h2>System Status</h2>
                <div id="status-content"></div>
            </div>

            <!-- Farm Info -->
            <div class="card">
                <h2>Farm Configuration</h2>
                <div id="farm-content"></div>
            </div>

            <!-- Weather/Radar -->
            <div class="card">
                <h2>Live Weather</h2>
                <div id="weather-content"></div>
            </div>

            <!-- Devices -->
            <div class="card">
                <h2>Connected Devices</h2>
                <div id="devices-content"></div>
            </div>
        </div>
    </div>

    <script src="{{ url_for('static', filename='app.js') }}"></script>
</body>
</html>
```

### Step 3: Create CSS Styling

Create file: `src/agriautonomous/web/static/style.css`

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

.navbar {
    background: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.status {
    font-size: 14px;
    padding: 8px 12px;
    background: #4caf50;
    border-radius: 5px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.card h2 {
    color: #333;
    margin-bottom: 15px;
    font-size: 20px;
    border-bottom: 2px solid #667eea;
    padding-bottom: 10px;
}

.metric {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}

.metric-label {
    font-weight: 600;
    color: #555;
}

.metric-value {
    color: #667eea;
    font-weight: bold;
}

.device-item {
    padding: 10px;
    margin: 5px 0;
    background: #f5f5f5;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.device-status {
    padding: 4px 8px;
    border-radius: 3px;
    font-size: 12px;
    font-weight: bold;
}

.device-status.online {
    background: #4caf50;
    color: white;
}

.device-status.offline {
    background: #f44336;
    color: white;
}

button {
    background: #667eea;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.3s ease;
}

button:hover {
    background: #764ba2;
}
```

### Step 4: Create JavaScript

Create file: `src/agriautonomous/web/static/app.js`

```javascript
// Fetch and display data
async function loadDashboard() {
    try {
        // Load status
        const status = await fetch('/api/status').then(r => r.json());
        document.getElementById('status-content').innerHTML = `
            <div class="metric">
                <span class="metric-label">Status:</span>
                <span class="metric-value">${status.status}</span>
            </div>
            <div class="metric">
                <span class="metric-label">Version:</span>
                <span class="metric-value">${status.version}</span>
            </div>
        `;

        // Load farm data
        const farm = await fetch('/api/farm').then(r => r.json());
        document.getElementById('farm-content').innerHTML = `
            <div class="metric">
                <span class="metric-label">Name:</span>
                <span class="metric-value">${farm.name || 'My Farm'}</span>
            </div>
            <div class="metric">
                <span class="metric-label">Latitude:</span>
                <span class="metric-value">${farm.latitude || 'N/A'}</span>
            </div>
            <div class="metric">
                <span class="metric-label">Longitude:</span>
                <span class="metric-value">${farm.longitude || 'N/A'}</span>
            </div>
        `;

        // Load weather
        const weather = await fetch('/api/radar/current').then(r => r.json());
        document.getElementById('weather-content').innerHTML = `
            <div class="metric">
                <span class="metric-label">Temperature:</span>
                <span class="metric-value">${weather.temperature}°C</span>
            </div>
            <div class="metric">
                <span class="metric-label">Wind Speed:</span>
                <span class="metric-value">${weather.wind_speed} km/h</span>
            </div>
            <div class="metric">
                <span class="metric-label">Precipitation:</span>
                <span class="metric-value">${weather.precipitation} mm</span>
            </div>
            <div class="metric">
                <span class="metric-label">Humidity:</span>
                <span class="metric-value">${weather.humidity}%</span>
            </div>
        `;

        // Load devices
        const devices = await fetch('/api/devices').then(r => r.json());
        let devicesHTML = '';
        devices.devices.forEach(device => {
            devicesHTML += `
                <div class="device-item">
                    <div>
                        <strong>${device.name}</strong>
                        <div style="font-size: 12px; color: #999;">${device.type}</div>
                    </div>
                    <span class="device-status ${device.status}">${device.status}</span>
                </div>
            `;
        });
        document.getElementById('devices-content').innerHTML = devicesHTML;

    } catch (error) {
        console.error('Error loading dashboard:', error);
        document.body.innerHTML += '<p style="color: red;">Error loading data</p>';
    }
}

// Load on page load and refresh every 30 seconds
window.onload = () => {
    loadDashboard();
    setInterval(loadDashboard, 30000);
};
```

### Step 5: Run Web Server

```bash
pip install flask flask-cors

python -m agriautonomous.web_server

# Access at: http://localhost:5000
# From network: http://<your-pc-ip>:5000
```

---

## Option 3: Background Service (Auto-Start)

### Windows - Task Scheduler

```batch
# Create batch file: agri-service.bat
@echo off
cd C:\path\to\Agriautonomus
call venv\Scripts\activate.bat
python -m agriautonomous.gui

# Then in Task Scheduler:
# 1. Open Task Scheduler
# 2. Create Basic Task
# 3. Set trigger: "At startup"
# 4. Action: "Start a program" → agri-service.bat
# 5. Check "Run with highest privileges"
```

### Linux - Systemd Service

Create: `/etc/systemd/system/agriautonomous.service`

```ini
[Unit]
Description=Agriautonomous Farming System
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/home/your-username/Agriautonomus
Environment="PATH=/home/your-username/Agriautonomus/venv/bin"
ExecStart=/home/your-username/Agriautonomus/venv/bin/python -m agriautonomous.web_server
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable agriautonomous
sudo systemctl start agriautonomous
sudo systemctl status agriautonomous
```

### macOS - Launch Agent

Create: `~/Library/LaunchAgents/com.agriautonomous.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.agriautonomous</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/Agriautonomus/venv/bin/python</string>
        <string>-m</string>
        <string>agriautonomous.web_server</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/agriautonomous.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/agriautonomous-error.log</string>
</dict>
</plist>
```

Enable:
```bash
launchctl load ~/Library/LaunchAgents/com.agriautonomous.plist
```

---

## Option 4: Local Network Deployment (Multi-Device)

### Step 1: Find Your PC IP Address

**Windows:**
```bash
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.100)
```

**Linux/macOS:**
```bash
ifconfig
hostname -I
```

### Step 2: Configure for Network Access

Edit: `src/agriautonomous/config.json`

```json
{
  "server": {
    "host": "0.0.0.0",
    "port": 5000,
    "allow_remote": true,
    "allowed_ips": ["192.168.1.*"]
  },
  "security": {
    "use_ssl": false,
    "require_auth": false
  }
}
```

### Step 3: Run Server

```bash
python -m agriautonomous.web_server
```

### Step 4: Access from Other Devices

From another device on the same network:
```
http://192.168.1.100:5000
```

---

## Option 5: Docker Container (Advanced)

### Step 1: Create Dockerfile

Create: `Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
COPY requirements-radar.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt -r requirements-radar.txt

# Copy application
COPY . .

# Install app
RUN pip install -e .

# Expose port
EXPOSE 5000

# Run web server
CMD ["python", "-m", "agriautonomous.web_server"]
```

### Step 2: Build Docker Image

```bash
docker build -t agriautonomous:local .
```

### Step 3: Run Container

```bash
docker run -p 5000:5000 \
  --name agri-local \
  -v ~/.agriautonomous:/root/.agriautonomous \
  agriautonomous:local
```

### Step 4: Access

```
http://localhost:5000
```

---

## Local Configuration

Create: `~/.agriautonomous/config.json`

```json
{
  "app": {
    "name": "Agriautonomous",
    "version": "2.0.0",
    "mode": "local"
  },
  "farm": {
    "name": "My Test Farm",
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  "radar": {
    "enabled": true,
    "offline_mode": true,
    "update_interval": 300,
    "cache_enabled": true
  },
  "server": {
    "host": "127.0.0.1",
    "port": 5000,
    "debug": false
  }
}
```

---

## Testing Local Deployment

```bash
# Test desktop app
Agriautonomous

# Test web server
curl http://localhost:5000/api/status

# Test from network
curl http://<your-pc-ip>:5000/api/status

# Run tests
pytest tests/ -v

# Check service status (Linux)
systemctl status agriautonomous
```

---

## Troubleshooting

**Port already in use:**
```bash
# Change port in config
# Use different port: 5001, 5002, etc.
python -m agriautonomous.web_server --port 5001
```

**Cannot connect from other devices:**
```bash
# Ensure firewall allows port 5000
# Windows: netsh advfirewall firewall add rule name="Agriautonomous" dir=in action=allow protocol=tcp localport=5000
# Linux: sudo ufw allow 5000
```

**Performance issues:**
```bash
# Run in production mode (no debug)
# Use gunicorn for production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 agriautonomous.web_server:app
```

---

## Summary of Deployment Options

| Method | Use Case | Complexity | Network |
|--------|----------|-----------|---------|
| **Desktop App** | Local testing | ⭐ Simple | None |
| **Web Server** | Browser access | ⭐⭐ Medium | LAN/Local |
| **Background Service** | Always running | ⭐⭐ Medium | None |
| **Network Deploy** | Multiple devices | ⭐⭐⭐ Complex | LAN |
| **Docker** | Containerized | ⭐⭐⭐⭐ Advanced | Any |

---

**You can now deploy locally on your PC! 🌾**
