"""Alert System"""
import uuid
from datetime import datetime
from typing import Dict, List
from enum import Enum
from loguru import logger

class AlertSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class AlertManager:
    """Manages system alerts"""
    
    def __init__(self):
        self.alerts = {}
        self.pending_alerts = []
    
    def create_alert(self, alert_type: str, message: str, 
                    severity: str = 'WARNING', asset_id: str = None) -> Dict:
        """Create new alert"""
        alert_id = str(uuid.uuid4())[:8]
        alert = {
            'alert_id': alert_id,
            'type': alert_type,
            'message': message,
            'severity': severity.upper(),
            'asset_id': asset_id,
            'created_at': datetime.utcnow().isoformat(),
            'status': 'pending'
        }
        
        self.alerts[alert_id] = alert
        self.pending_alerts.append(alert_id)
        
        log_func = logger.critical if severity == 'CRITICAL' else logger.warning
        log_func(f"Alert [{alert_type}]: {message}")
        
        return alert
    
    def get_alerts(self, status: str = None) -> List[Dict]:
        """Get alerts"""
        alerts = list(self.alerts.values())
        if status:
            alerts = [a for a in alerts if a['status'] == status]
        return alerts
    
    def acknowledge_alert(self, alert_id: str) -> bool:
        """Acknowledge alert"""
        if alert_id not in self.alerts:
            return False
        
        alert = self.alerts[alert_id]
        alert['status'] = 'acknowledged'
        if alert_id in self.pending_alerts:
            self.pending_alerts.remove(alert_id)
        
        logger.info(f"Alert acknowledged: {alert_id}")
        return True
    
    def resolve_alert(self, alert_id: str) -> bool:
        """Resolve alert"""
        if alert_id not in self.alerts:
            return False
        
        alert = self.alerts[alert_id]
        alert['status'] = 'resolved'
        alert['resolved_at'] = datetime.utcnow().isoformat()
        
        logger.info(f"Alert resolved: {alert_id}")
        return True
    
    def count_pending(self) -> int:
        """Count pending alerts"""
        return len(self.pending_alerts)

alert_manager = AlertManager()
