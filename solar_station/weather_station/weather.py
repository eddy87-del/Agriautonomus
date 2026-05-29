"""Weather Station Module"""
from loguru import logger

class WeatherStation:
    """Monitors weather conditions"""
    
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.wind_speed = 0.0
        self.wind_direction = 0.0
        self.rainfall = 0.0
    
    def get_weather(self) -> dict:
        """Get current weather"""
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'wind_direction': self.wind_direction,
            'rainfall': self.rainfall
        }
    
    def check_flight_conditions(self) -> bool:
        """Check if conditions are safe for flight"""
        logger.info(f"Checking flight conditions - Wind: {self.wind_speed} m/s")
        return self.wind_speed < 10.0
