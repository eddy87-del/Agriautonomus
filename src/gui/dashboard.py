"""Dashboard widget"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class DashboardWidget(QWidget):
    """Dashboard widget showing system status"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel('System Status'))
        layout.addWidget(QPushButton('Refresh'))
        self.setLayout(layout)
