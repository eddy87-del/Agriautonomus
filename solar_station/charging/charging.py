"""Solar Station Charging System"""
from loguru import logger

class ChargingSystem:
    """Manages charging for drones and UGV"""
    
    def __init__(self):
        self.charging_bays = {
            'scout_drone': {'charging': False, 'level': 0.0},
            'action_drone': {'charging': False, 'level': 0.0},
            'ugv': {'charging': False, 'level': 0.0}
        }
    
    def start_charging(self, asset_type: str) -> bool:
        """Start charging asset"""
        if asset_type in self.charging_bays:
            logger.info(f"Starting charging for {asset_type}")
            self.charging_bays[asset_type]['charging'] = True
            return True
        return False
    
    def stop_charging(self, asset_type: str) -> bool:
        """Stop charging asset"""
        if asset_type in self.charging_bays:
            logger.info(f"Stopping charging for {asset_type}")
            self.charging_bays[asset_type]['charging'] = False
            return True
        return False
    
    def get_charge_level(self, asset_type: str) -> float:
        """Get charge level"""
        if asset_type in self.charging_bays:
            return self.charging_bays[asset_type]['level']
        return 0.0
