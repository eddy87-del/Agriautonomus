"""User Manual"""

# Agriautonomous User Manual

## Getting Started

### Launching the Application

1. **Windows:** Click Agriautonomous in Start Menu or Desktop
2. **Linux:** Click Agriautonomous in Applications menu
3. **macOS:** Click Agriautonomous in Applications folder

### Initial Setup

1. **Welcome Screen** - Review system information
2. **Farm Configuration** - Enter farm details:
   - Farm name
   - Location (GPS coordinates)
   - Field area
   - Soil type
3. **Hardware Registration** - Add devices:
   - Scout Drone
   - Action Drone
   - Ground Robot (UGV)
   - Solar Station
4. **Communication Setup** - Configure connection:
   - Serial port
   - Baud rate
   - Network settings (optional)

## Main Interface

### Dashboard

Shows system overview:
- Active assets status
- Battery levels
- GPS positions
- Current alerts
- System metrics

### Missions Tab

**Create Mission:**
1. Click "New Mission"
2. Select mission type:
   - Survey/Mapping
   - Spraying
   - Weeding
   - Planting
3. Define waypoints on map
4. Set parameters (altitude, speed, etc.)
5. Save mission

**Execute Mission:**
1. Select mission from list
2. Click "Arm" - prepares asset
3. Click "Execute" - starts mission
4. Monitor progress
5. Click "Abort" if needed

### Assets Tab

**Register Asset:**
1. Click "Add Asset"
2. Select type (Drone/Robot/Station)
3. Enter ID and name
4. Set parameters
5. Click "Save"

**Monitor Asset:**
1. Select asset from list
2. View status, battery, position
3. Check telemetry data
4. View error history

### Alerts Tab

**Alert Types:**
- Battery low
- GPS signal lost
- Mission timeout
- Hardware error
- Geofence breach

**Managing Alerts:**
1. View pending alerts
2. Click to acknowledge
3. Review details
4. Take action or dismiss

### Settings Tab

**System Settings:**
- Theme (Light/Dark)
- Language
- Auto-start on boot
- Debug logging

**Hardware Settings:**
- Serial port configuration
- Communication parameters
- Device timeouts

**Advanced Settings:**
- Database location
- Log retention
- Network configuration

## Command Line Interface

### Basic Commands

```bash
# Check system status
agri system status

# List all assets
agri list assets

# Get asset details
agri asset status SCOUT_DRONE_001

# Create mission
agri create mission --name "Field Survey" --type survey

# Arm mission
agri arm mission MISSION_001

# Execute mission
agri execute mission MISSION_001

# View logs
agri logs --follow
```

## Best Practices

### Mission Planning

1. **Check Weather** - Verify wind speed < 10 m/s
2. **Charge Assets** - Ensure batteries at 100%
3. **Test Mission** - Use simulator mode first
4. **Plan Waypoints** - Keep within geofence
5. **Set RTH Altitude** - Return-to-home height

### Field Operations

1. **Clear Field** - Remove obstacles
2. **Calibrate Compass** - Before first mission
3. **Test Communications** - Verify telemetry link
4. **Monitor Progress** - Watch dashboard
5. **Log Results** - Record mission data

### Maintenance

1. **Weekly Checks**
   - Clean sensors
   - Inspect propellers
   - Check batteries
   - Update firmware

2. **Monthly Maintenance**
   - Recalibrate IMU
   - Check motor bearings
   - Clean solar panels
   - Backup data

## Troubleshooting

### Common Issues

**"Device Not Found"**
- Check USB cable
- Verify serial port (agri hardware --scan)
- Reinstall drivers
- Try different USB port

**"GPS No Fix"**
- Move to open sky
- Wait 30+ seconds
- Check antenna connection
- Verify GPS module powered

**"Mission Failed"**
- Check battery level
- Verify GPS signal
- Review error logs
- Check weather conditions

**"No Telemetry Data"**
- Verify radio connection
- Check serial port
- Confirm baud rate
- Test with CLI

## Support

- **Documentation:** https://agriautonomous.readthedocs.io
- **FAQ:** https://github.com/eddy87-del/Agriautonomus/wiki
- **Issues:** https://github.com/eddy87-del/Agriautonomus/issues
- **Email:** support@agriautonomous.com
