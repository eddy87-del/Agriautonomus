"""Telemetry Data Collection and Management"""
import json
from datetime import datetime
from typing import Dict, List
from loguru import logger

class TelemetryCollector:
    """Collects and manages telemetry from all assets"""
    
    def __init__(self):
        self.telemetry_store = {}
    
    def collect(self, asset_id: str, data: Dict):
        """Collect telemetry from asset"""
        timestamp = datetime.utcnow().isoformat()
        telemetry_entry = {
            'timestamp': timestamp,
            'asset_id': asset_id,
            **data
        }
        
        if asset_id not in self.telemetry_store:
            self.telemetry_store[asset_id] = []
        
        self.telemetry_store[asset_id].append(telemetry_entry)
        logger.debug(f"Telemetry collected from {asset_id}")
        return telemetry_entry
    
    def get_latest(self, asset_id: str) -> Dict:
        """Get latest telemetry for asset"""
        if asset_id in self.telemetry_store and self.telemetry_store[asset_id]:
            return self.telemetry_store[asset_id][-1]
        return {}
    
    def get_history(self, asset_id: str, limit: int = 100) -> List[Dict]:
        """Get telemetry history"""
        if asset_id not in self.telemetry_store:
            return []
        return self.telemetry_store[asset_id][-limit:]

telemetry_collector = TelemetryCollector()
