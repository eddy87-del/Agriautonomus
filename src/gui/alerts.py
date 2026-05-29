"""Alerts widget"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

class AlertsWidget(QWidget):
    """Alerts display widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel('System Alerts'))
        layout.addWidget(QListWidget())
        layout.addWidget(QPushButton('Acknowledge'))
        layout.addWidget(QPushButton('Clear'))
        self.setLayout(layout)
