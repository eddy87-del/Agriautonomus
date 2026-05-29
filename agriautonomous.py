"""Main application entry point"""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from loguru import logger
import os

def setup_logging():
    """Setup application logging"""
    log_dir = Path.home() / '.agriautonomous' / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logger.remove()
    logger.add(
        log_dir / 'agriautonomous.log',
        rotation='500 MB',
        retention='10 days',
        level='INFO'
    )
    logger.add(sys.stderr, level='DEBUG')

def setup_data_dir():
    """Setup application data directory"""
    data_dir = Path.home() / '.agriautonomous'
    data_dir.mkdir(exist_ok=True)
    
    (data_dir / 'config').mkdir(exist_ok=True)
    (data_dir / 'logs').mkdir(exist_ok=True)
    (data_dir / 'data').mkdir(exist_ok=True)
    (data_dir / 'missions').mkdir(exist_ok=True)
    
    return data_dir

def main():
    """Main application entry point"""
    # Setup
    setup_logging()
    data_dir = setup_data_dir()
    
    logger.info("=" * 60)
    logger.info("Starting Agriautonomous Desktop Application")
    logger.info(f"Data directory: {data_dir}")
    logger.info("=" * 60)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName('Agriautonomous')
    app.setApplicationVersion('2.0.0')
    
    # Create main window
    window = MainWindow()
    window.show()
    
    logger.info("Application started successfully")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
