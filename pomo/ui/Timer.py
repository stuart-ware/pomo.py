
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PySide6 import QtCore, QtGui
import sys

class Timer(QWidget):
    def __init__(self):
        super().__init__()

        # window properties
        self.PROGRAM_VERSION = "0.2.0"
        self.font = QtGui.QFont("JetBrainsMono Nerd Font", 10)
        self.setFixedSize(QtCore.QSize(200,200))
        self.setStyleSheet("background-color: #2cde85")

        # timer
        self.minutes = 0
        self.seconds = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)
         
        # label
        self.image = QLabel(self)
        self.pixmap = QtGui.QPixmap(".//src//images//pomo.png")
        self.image.setPixmap(self.pixmap)

        self.program = QLabel(f"pomo.py {self.PROGRAM_VERSION}", self)
        self.count = QLabel("READY!", self)

        # buttons
        self.button_start = QPushButton(self)
        self.button_stop = QPushButton(self)
        self.button_rest = QPushButton(self)
        self.button_about = QPushButton(self)

        # label configs
        self.program.setGeometry(51, 125, 110, 20)
        self.program.setFont(self.font)
        self.program.setStyleSheet("color: #f1f1f1")

        self.image.move(10, 3)

        self.count.move(30, 65)
        self.count_font = QtGui.QFont("JetBrainsMono Nerd Font", 30)
        self.count.setFont(self.count_font)
        self.count.setStyleSheet("color: #f1f1f1")

        # button configs
        self.button_start.setGeometry(65, 150, 30, 30)
        self.button_start.setIcon(QtGui.QIcon(".//src//images//play.png"))
        self.button_start.setIconSize(QtCore.QSize(30,30))

        self.button_about.setGeometry(160, 10, 30, 30)
        self.button_about.setIcon(QtGui.QIcon(".//src//images//about.png"))
        self.button_about.setIconSize(QtCore.QSize(30,30))

        self.button_stop.hide()
        self.button_rest.setGeometry(105, 150, 30, 30)
        self.button_rest.setIcon(QtGui.QIcon(".//src//images//rest.png"))
        self.button_rest.setIconSize(QtCore.QSize(30,30))

        # link
        self.button_start.clicked.connect(self.start_pomo)
        self.button_stop.clicked.connect(self.stop)
        self.button_rest.clicked.connect(self.start_rest)
        self.button_about.clicked.connect(self.about)

    @QtCore.Slot()
    def start_pomo(self):
        self.minutes = 25
        self.seconds = 0
        self.setStyleSheet("background-color: #d92404")
        self.count.setText("FOCUS")
        self.count.move(40, 65)

        self.button_start.hide()
        self.button_rest.hide()

        self.button_stop.setGeometry(85, 150, 30, 30)
        self.button_stop.setIcon(QtGui.QIcon(".//src//images//stop.png"))
        self.button_stop.setIconSize(QtCore.QSize(30,30))

        self.button_stop.show()
        self.timer.start()

    @QtCore.Slot()
    def start_rest(self):
        self.minutes = 5
        self.seconds = 0
        self.setStyleSheet("background-color: #079dd9")
        self.count.setText("REST!")
        self.count.move(40, 65)

        self.button_start.hide()
        self.button_rest.hide()

        self.button_stop.setGeometry(85, 150, 30, 30)
        self.button_stop.setIcon(QtGui.QIcon(".//src//images//stop.png"))
        self.button_stop.setIconSize(QtCore.QSize(30,30))

        self.button_stop.show()
        self.timer.start()

    @QtCore.Slot()
    def stop(self):
        self.setStyleSheet("background-color: #2cde85")
        self.count.setText("DONE!")

        self.button_stop.hide()

        self.button_start.show()
        self.button_rest.show()
        self.timer.stop()
        self.notifications()
    
    @QtCore.Slot()
    def about(self):
        self.about_window = None
        
        if self.about_window is None:
            self.about_window = About()
            self.about_window.destroyed.connect(About)
        self.about_window.show()
    
    @QtCore.Slot()
    def update_timer(self):
        self.count.setText(f"{self.minutes:02}:{self.seconds:02}")
        
        if self.seconds <= 0:
            self.seconds = 59
            if self.minutes != 0:
                self.minutes -= 1
            else:
                self.minutes = 0
        elif self.seconds == 1 and self.minutes == 0:
            self.stop()
            self.timer.stop()
        else:
            self.seconds -= 1
    
    @QtCore.Slot()
    def notifications(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = Timer()
    window.show()
    sys.exit(app.exec())