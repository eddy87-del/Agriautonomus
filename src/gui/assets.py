"""Assets widget"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

class AssetsWidget(QWidget):
    """Assets registry widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Registered Assets'))
        layout.addWidget(QListWidget())
        layout.addWidget(QPushButton('Add Asset'))
        layout.addWidget(QPushButton('Remove Asset'))
        self.setLayout(layout)
