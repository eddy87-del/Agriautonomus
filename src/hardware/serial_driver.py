"""Serial communication driver"""
import serial
from loguru import logger

class SerialDriver:
    """Serial port communication driver"""
    
    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 57600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
    
    def connect(self) -> bool:
        """Connect to serial port"""
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )
            logger.info(f"Connected to {self.port} at {self.baudrate} baud")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to {self.port}: {e}")
            return False
    
    def send(self, data: bytes) -> bool:
        """Send data"""
        if not self.serial or not self.serial.is_open:
            return False
        try:
            self.serial.write(data)
            return True
        except Exception as e:
            logger.error(f"Send error: {e}")
            return False
    
    def receive(self, size: int = 1024) -> bytes:
        """Receive data"""
        if not self.serial or not self.serial.is_open:
            return b''
        try:
            return self.serial.read(size)
        except Exception as e:
            logger.error(f"Receive error: {e}")
            return b''
    
    def disconnect(self):
        """Disconnect from serial port"""
        if self.serial and self.serial.is_open:
            self.serial.close()
            logger.info(f"Disconnected from {self.port}")
