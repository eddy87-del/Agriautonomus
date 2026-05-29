"""CLI help for hardware commands"""

# Hardware Commands

## Scanning

```bash
agri hardware --scan
```

Scans for connected hardware devices and displays:
- Serial ports
- Device types
- Connection status
- Firmware versions

## Configuration

```bash
agri hardware --config /dev/ttyUSB0 --baud 57600
```

Configures hardware connection parameters.

## Testing

```bash
agri hardware --test DEVICE_ID
```

Runs diagnostic test on device.

## Firmware

```bash
agri hardware --firmware update DEVICE_ID
agri hardware --firmware info DEVICE_ID
```

Manages device firmware updates.

## Status

```bash
agri hardware --status
```

Shows all connected hardware status.
