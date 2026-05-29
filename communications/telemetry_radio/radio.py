"""Telemetry Radio Module"""
from loguru import logger
import serial

class TelemetryRadio:
    """Telemetry radio communication"""
    
    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 57600):
        self.port = port
        self.baudrate = baudrate
        self.serial_port = None
    
    def connect(self) -> bool:
        """Connect to telemetry radio"""
        try:
            logger.info(f"Connecting to telemetry radio on {self.port}")
            self.serial_port = serial.Serial(self.port, self.baudrate)
            return True
        except Exception as e:
            logger.error(f"Telemetry radio connection failed: {e}")
            return False
    
    def send_data(self, data: bytes) -> bool:
        """Send data via telemetry radio"""
        if self.serial_port:
            self.serial_port.write(data)
            return True
        return False
    
    def receive_data(self) -> bytes:
        """Receive data from telemetry radio"""
        if self.serial_port:
            return self.serial_port.read()
        return b''
