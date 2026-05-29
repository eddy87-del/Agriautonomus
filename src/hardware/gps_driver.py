"""GPS driver"""
from loguru import logger

class GPSDriver:
    """GPS hardware driver"""
    
    def __init__(self, serial_driver):
        self.serial = serial_driver
        self.position = (0.0, 0.0, 0.0)
    
    def get_position(self) -> tuple:
        """Get current position"""
        logger.debug(f"GPS position: {self.position}")
        return self.position
    
    def update_position(self):
        """Update position from GPS"""
        logger.debug("Updating GPS position")
