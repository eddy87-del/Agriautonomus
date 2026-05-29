"""Asset registry"""
import json
from pathlib import Path
from datetime import datetime
from loguru import logger

class AssetRegistry:
    """Manages asset registry"""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir / 'data'
        self.data_dir.mkdir(exist_ok=True)
        self.assets_file = self.data_dir / 'assets.json'
        self.assets = self.load_assets()
    
    def load_assets(self) -> dict:
        """Load assets from disk"""
        if self.assets_file.exists():
            with open(self.assets_file) as f:
                return json.load(f)
        return {}
    
    def save_assets(self):
        """Save assets to disk"""
        with open(self.assets_file, 'w') as f:
            json.dump(self.assets, f, indent=2)
    
    def register_asset(self, asset_data: dict) -> dict:
        """Register new asset"""
        asset_id = asset_data.get('id')
        if not asset_id:
            return {'success': False, 'error': 'Asset ID required'}
        
        asset = {
            'id': asset_id,
            'name': asset_data.get('name', asset_id),
            'type': asset_data.get('type'),
            'status': 'offline',
            'battery': 100.0,
            'registered_at': datetime.utcnow().isoformat(),
            **asset_data
        }
        
        self.assets[asset_id] = asset
        self.save_assets()
        logger.info(f"Asset registered: {asset_id}")
        return {'success': True, 'asset': asset}
    
    def get_asset(self, asset_id: str) -> dict:
        """Get asset details"""
        return self.assets.get(asset_id)
    
    def list_assets(self) -> list:
        """List all assets"""
        return list(self.assets.values())
    
    def update_asset(self, asset_id: str, data: dict) -> bool:
        """Update asset"""
        if asset_id not in self.assets:
            return False
        
        self.assets[asset_id].update(data)
        self.save_assets()
        logger.info(f"Asset updated: {asset_id}")
        return True
    
    def unregister_asset(self, asset_id: str) -> bool:
        """Unregister asset"""
        if asset_id not in self.assets:
            return False
        
        del self.assets[asset_id]
        self.save_assets()
        logger.info(f"Asset unregistered: {asset_id}")
        return True
