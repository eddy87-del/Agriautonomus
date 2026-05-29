"""Mission Management System"""
import uuid
from datetime import datetime
from typing import Dict, List
from enum import Enum
from loguru import logger

class MissionStatus(Enum):
    PLANNED = "planned"
    ARMED = "armed"
    EXECUTING = "executing"
    PAUSED = "paused"
    COMPLETED = "completed"
    ABORTED = "aborted"

class MissionManager:
    """Manages all missions"""
    
    def __init__(self):
        self.missions = {}
        self.active_missions = []
    
    def create_mission(self, mission_data: Dict) -> Dict:
        """Create new mission"""
        mission_id = str(uuid.uuid4())[:8]
        mission = {
            'mission_id': mission_id,
            'name': mission_data.get('name'),
            'asset_id': mission_data.get('asset_id'),
            'mission_type': mission_data.get('mission_type'),
            'status': MissionStatus.PLANNED.value,
            'waypoints': mission_data.get('waypoints', []),
            'parameters': mission_data.get('parameters', {}),
            'created_at': datetime.utcnow().isoformat(),
            'priority': mission_data.get('priority', 'normal')
        }
        
        self.missions[mission_id] = mission
        logger.info(f"Mission created: {mission_id}")
        return mission
    
    def get_mission(self, mission_id: str) -> Dict:
        """Get mission details"""
        return self.missions.get(mission_id, {})
    
    def list_missions(self, status: str = None) -> List[Dict]:
        """List all missions"""
        missions = list(self.missions.values())
        if status:
            missions = [m for m in missions if m['status'] == status]
        return missions
    
    def arm_mission(self, mission_id: str) -> bool:
        """Arm mission for execution"""
        if mission_id not in self.missions:
            return False
        
        mission = self.missions[mission_id]
        if mission['status'] != MissionStatus.PLANNED.value:
            return False
        
        mission['status'] = MissionStatus.ARMED.value
        logger.info(f"Mission armed: {mission_id}")
        return True
    
    def execute_mission(self, mission_id: str) -> bool:
        """Execute armed mission"""
        if mission_id not in self.missions:
            return False
        
        mission = self.missions[mission_id]
        if mission['status'] != MissionStatus.ARMED.value:
            return False
        
        mission['status'] = MissionStatus.EXECUTING.value
        mission['started_at'] = datetime.utcnow().isoformat()
        self.active_missions.append(mission_id)
        logger.info(f"Mission executing: {mission_id}")
        return True
    
    def abort_mission(self, mission_id: str) -> bool:
        """Abort mission"""
        if mission_id not in self.missions:
            return False
        
        mission = self.missions[mission_id]
        mission['status'] = MissionStatus.ABORTED.value
        if mission_id in self.active_missions:
            self.active_missions.remove(mission_id)
        logger.warning(f"Mission aborted: {mission_id}")
        return True

mission_manager = MissionManager()
