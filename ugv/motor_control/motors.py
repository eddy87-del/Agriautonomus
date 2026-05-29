"""Motor Control System"""
from loguru import logger

class MotorController:
    """Controls UGV motors"""
    
    def __init__(self):
        self.left_speed = 0.0
        self.right_speed = 0.0
    
    def set_speed(self, left: float, right: float):
        """Set motor speeds"""
        self.left_speed = left
        self.right_speed = right
        logger.debug(f"Motor speeds: L={left}, R={right}")
    
    def move_forward(self, speed: float):
        """Move forward"""
        self.set_speed(speed, speed)
        logger.info(f"Moving forward at {speed}")
    
    def turn_left(self, speed: float):
        """Turn left"""
        self.set_speed(speed * 0.5, speed)
        logger.info("Turning left")
    
    def turn_right(self, speed: float):
        """Turn right"""
        self.set_speed(speed, speed * 0.5)
        logger.info("Turning right")
    
    def stop(self):
        """Stop motors"""
        self.set_speed(0, 0)
        logger.info("Motors stopped")
