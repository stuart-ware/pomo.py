from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PySide6 import QtCore, QtGui
class About(QWidget):
    def __init__(self):
        super().__init__()
        
        self.font = QtGui.QFont("JetBrainsMono Nerd Font", 8)
            
        self.setFixedSize(QtCore.QSize(300,200))
        self.setFont(self.font)
        self.setStyleSheet("background-color: #1f1f1f")

        self.logo = QLabel(self)
        logop = QtGui.QPixmap(".//src//images//pomo1.png")
        self.logo.setPixmap(logop)

        self.stuart = QLabel(self)
        stuart_logo = QtGui.QPixmap(".//src//images//stsoft.png")
        self.stuart.setPixmap(stuart_logo) 
        
        self.logo.move(50, 6)
        self.stuart.move(50, 80)

        self.credits = QLabel("pomo.py 0.2.0 by @stuartsoftware on GitHub\nThis is pomo.py a pomodoro app\nmade in Python and Qt", self)
        
        self.credits.setStyleSheet("color: #f1f1f1")
        self.credits.move(12, 145)
        self.credits.setAlignment(QtCore.Qt.AlignCenter)