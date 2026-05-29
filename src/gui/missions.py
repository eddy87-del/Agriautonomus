"""Missions widget"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

class MissionsWidget(QWidget):
    """Missions management widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Active Missions'))
        layout.addWidget(QListWidget())
        layout.addWidget(QPushButton('New Mission'))
        layout.addWidget(QPushButton('Delete Mission'))
        self.setLayout(layout)
