"""Action Drone Implementation"""
from loguru import logger

class ActionDrone:
    """Action drone for spraying and payload delivery"""
    
    def __init__(self, drone_id: str):
        self.drone_id = drone_id
        self.status = 'idle'
        self.battery = 100.0
        self.spray_tank = 5.0  # liters
        self.position = (0, 0, 0)
    
    def arm(self) -> bool:
        """Arm drone"""
        logger.info(f"Arming action drone {self.drone_id}")
        self.status = 'armed'
        return True
    
    def start_spray(self) -> bool:
        """Start spraying"""
        logger.info(f"Starting spray on drone {self.drone_id}")
        return True
    
    def stop_spray(self) -> bool:
        """Stop spraying"""
        logger.info(f"Stopping spray on drone {self.drone_id}")
        return True
    
    def enable_bird_deterrence(self) -> bool:
        """Enable bird deterrence"""
        logger.info(f"Enabling bird deterrence on drone {self.drone_id}")
        return True
    
    def drop_payload(self) -> bool:
        """Drop payload"""
        logger.info(f"Dropping payload from drone {self.drone_id}")
        return True
