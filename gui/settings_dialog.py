# settings_dialog.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNC Settings")
        self.setGeometry(100, 100, 400, 300)
        
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.spindle_speed = QLineEdit(self)
        self.spindle_speed.setPlaceholderText("Enter spindle speed")
        layout.addWidget(self.spindle_speed)
        
        self.feed_rate = QLineEdit(self)
        self.feed_rate.setPlaceholderText("Enter feed rate")
        layout.addWidget(self.feed_rate)

        save_button = QPushButton("Save Settings", self)
        layout.addWidget(save_button)
        
        self.setLayout(layout)
