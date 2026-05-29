"""Database initialization"""
from pathlib import Path
from loguru import logger

class Database:
    """Database manager"""
    
    def __init__(self, db_path: str):
        self.db_path = Path(db_path).expanduser()
        self.init_database()
    
    def init_database(self):
        """Initialize database"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Database initialized at {self.db_path}")
