"""Mission execution service"""
from threading import Thread
from loguru import logger
import time

class MissionService:
    """Background mission execution service"""
    
    def __init__(self, config, mission_manager):
        self.config = config
        self.mission_manager = mission_manager
        self.running = False
        self.thread = None
        self.current_mission = None
    
    def start(self):
        """Start mission service"""
        if self.running:
            return
        
        self.running = True
        self.thread = Thread(target=self._run, daemon=True)
        self.thread.start()
        logger.info("Mission service started")
    
    def stop(self):
        """Stop mission service"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        logger.info("Mission service stopped")
    
    def execute_mission(self, mission_id: str):
        """Execute mission"""
        mission = self.mission_manager.get_mission(mission_id)
        if mission:
            self.current_mission = mission
            logger.info(f"Executing mission: {mission_id}")
    
    def _run(self):
        """Service loop"""
        while self.running:
            try:
                if self.current_mission:
                    logger.debug(f"Processing mission: {self.current_mission['id']}")
                
                time.sleep(1)
            except Exception as e:
                logger.error(f"Mission service error: {e}")
                time.sleep(1)
