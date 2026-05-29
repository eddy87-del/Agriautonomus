"""Main application window"""
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QPushButton, QStatusBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from loguru import logger

class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Agriautonomous Control Center')
        self.setGeometry(100, 100, 1200, 800)
        
        logger.info("Initializing main window")
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout(central_widget)
        
        # Create tabs
        tabs = QTabWidget()
        tabs.addTab(self.create_dashboard_tab(), 'Dashboard')
        tabs.addTab(self.create_missions_tab(), 'Missions')
        tabs.addTab(self.create_assets_tab(), 'Assets')
        tabs.addTab(self.create_alerts_tab(), 'Alerts')
        tabs.addTab(self.create_settings_tab(), 'Settings')
        
        layout.addWidget(tabs)
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Ready')
        
        logger.info("Main window initialized")
    
    def create_dashboard_tab(self):
        """Create dashboard tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Dashboard'))
        widget.setLayout(layout)
        return widget
    
    def create_missions_tab(self):
        """Create missions tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Missions Control'))
        layout.addWidget(QPushButton('New Mission'))
        layout.addWidget(QPushButton('Arm'))
        layout.addWidget(QPushButton('Execute'))
        layout.addWidget(QPushButton('Abort'))
        widget.setLayout(layout)
        return widget
    
    def create_assets_tab(self):
        """Create assets tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Assets Registry'))
        widget.setLayout(layout)
        return widget
    
    def create_alerts_tab(self):
        """Create alerts tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('System Alerts'))
        widget.setLayout(layout)
        return widget
    
    def create_settings_tab(self):
        """Create settings tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Settings'))
        widget.setLayout(layout)
        return widget
