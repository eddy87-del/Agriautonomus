"""Background telemetry service"""
from threading import Thread
from loguru import logger
import time

class TelemetryService:
    """Background telemetry collection service"""
    
    def __init__(self, config, asset_registry):
        self.config = config
        self.asset_registry = asset_registry
        self.running = False
        self.thread = None
    
    def start(self):
        """Start telemetry service"""
        if self.running:
            return
        
        self.running = True
        self.thread = Thread(target=self._run, daemon=True)
        self.thread.start()
        logger.info("Telemetry service started")
    
    def stop(self):
        """Stop telemetry service"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        logger.info("Telemetry service stopped")
    
    def _run(self):
        """Service loop"""
        interval = self.config.get('telemetry.interval', 1)
        
        while self.running:
            try:
                # Collect telemetry from all assets
                for asset in self.asset_registry.list_assets():
                    logger.debug(f"Collecting telemetry from {asset['id']}")
                
                time.sleep(interval)
            except Exception as e:
                logger.error(f"Telemetry service error: {e}")
                time.sleep(1)
