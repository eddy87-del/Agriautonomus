"""Simulation Environment"""
from loguru import logger

class SimulationEnvironment:
    """Simulates farm environment and assets"""
    
    def __init__(self):
        self.time = 0
        self.assets = {}
    
    def add_asset(self, asset_id: str, asset_type: str):
        """Add asset to simulation"""
        logger.info(f"Adding {asset_type} to simulation")
        self.assets[asset_id] = {'type': asset_type, 'status': 'idle'}
    
    def run_simulation(self, duration: int = 3600):
        """Run simulation"""
        logger.info(f"Running simulation for {duration}s")
    
    def step(self):
        """Execute one simulation step"""
        self.time += 1
