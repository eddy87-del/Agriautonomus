"""Application configuration"""
import json
from pathlib import Path
from loguru import logger

class Config:
    """Application configuration manager"""
    
    DEFAULT_CONFIG = {
        'app_name': 'Agriautonomous',
        'app_version': '2.0.0',
        'theme': 'dark',
        'language': 'en',
        'auto_start': False,
        'debug': False,
        'hardware': {
            'serial_port': '/dev/ttyUSB0',
            'baudrate': 57600,
            'timeout': 5
        },
        'telemetry': {
            'interval': 1,
            'buffer_size': 1000
        },
        'database': {
            'type': 'sqlite',
            'path': '~/.agriautonomous/data/agriautonomous.db'
        }
    }
    
    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self.config_file = config_dir / 'config.json'
        self.config = self.load_config()
    
    def load_config(self) -> dict:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file) as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading config: {e}")
                return self.DEFAULT_CONFIG.copy()
        else:
            self.save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()
    
    def save_config(self, config: dict = None):
        """Save configuration to file"""
        if config:
            self.config = config
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info(f"Configuration saved to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving config: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value else default
    
    def set(self, key: str, value):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save_config()
        logger.info(f"Configuration updated: {key}")
