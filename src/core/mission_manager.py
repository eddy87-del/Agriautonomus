"""Mission management"""
import json
from pathlib import Path
from datetime import datetime
from loguru import logger

class MissionManager:
    """Manages missions locally"""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir / 'missions'
        self.data_dir.mkdir(exist_ok=True)
        self.missions = {}
    
    def create_mission(self, mission_data: dict) -> dict:
        """Create new mission"""
        mission_id = mission_data.get('id', f'MISSION_{datetime.now().timestamp()}')
        mission = {
            'id': mission_id,
            'name': mission_data.get('name', 'Untitled'),
            'status': 'planned',
            'created_at': datetime.utcnow().isoformat(),
            **mission_data
        }
        
        self.missions[mission_id] = mission
        self.save_mission(mission)
        logger.info(f"Mission created: {mission_id}")
        return mission
    
    def save_mission(self, mission: dict):
        """Save mission to disk"""
        mission_file = self.data_dir / f"{mission['id']}.json"
        with open(mission_file, 'w') as f:
            json.dump(mission, f, indent=2)
    
    def load_mission(self, mission_id: str) -> dict:
        """Load mission from disk"""
        mission_file = self.data_dir / f"{mission_id}.json"
        if mission_file.exists():
            with open(mission_file) as f:
                return json.load(f)
        return None
    
    def list_missions(self) -> list:
        """List all missions"""
        return list(self.missions.values())
    
    def get_mission(self, mission_id: str) -> dict:
        """Get mission details"""
        return self.missions.get(mission_id)
    
    def update_mission(self, mission_id: str, data: dict) -> bool:
        """Update mission"""
        if mission_id not in self.missions:
            return False
        
        self.missions[mission_id].update(data)
        self.save_mission(self.missions[mission_id])
        logger.info(f"Mission updated: {mission_id}")
        return True
    
    def delete_mission(self, mission_id: str) -> bool:
        """Delete mission"""
        if mission_id not in self.missions:
            return False
        
        mission_file = self.data_dir / f"{mission_id}.json"
        if mission_file.exists():
            mission_file.unlink()
        
        del self.missions[mission_id]
        logger.info(f"Mission deleted: {mission_id}")
        return True
