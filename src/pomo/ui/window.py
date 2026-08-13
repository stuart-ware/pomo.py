from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from pomo.core import timer
from pomo.var import FONT, PROGRAM_VERSION


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(f"pomo.py {PROGRAM_VERSION}")
        self.program_font: QtGui.QFont = QtGui.QFont(FONT, 10)
        self.setFixedSize(QtCore.QSize(200,200))
        
        # Labels
        self.program_name: QLabel = QLabel(f"pomo.py {PROGRAM_VERSION}", self)
        self.program_name.setFont(QtGui.QFont(FONT, 8))
        self.program_name.move(56, 180)

        self.timer: QLabel = QLabel("START", self)
        self.timer.setFont(QtGui.QFont(FONT, 45))
        self.timer.move(10, 50)

        self.timer_logic: timer.Timer = timer.Timer()
        self.timer_logic.tick.connect(self._update_label)  # pyright: ignore[reportUnusedCallResult]

        # Buttons
        self.start_button: QPushButton = QPushButton(self)
        self.start_button.setGeometry(80, 145, 45, 30)
        self.start_button.clicked.connect(self._start)  # pyright: ignore[reportUnusedCallResult]
        self.start_button.setText("START")

        self.stop_button: QPushButton = QPushButton(self)
        self.stop_button.setGeometry(80, 145, 45, 30)
        self.stop_button.clicked.connect(self._stop)  # pyright: ignore[reportUnusedCallResult]
        self.stop_button.setText("STOP")
        self.stop_button.setVisible(False)


    def _update_label(self, minutes: int, seconds: int):
        self.timer.setText(f"{minutes:02d}:{seconds:02d}")
        if minutes == 0 and seconds == 0:
            self.timer.move(28, 50)
            self.timer.setText("DONE")
            
    def _stop(self):
        self.timer_logic.stop()
        self.start_button.setVisible(True)
        self.stop_button.setVisible(False)

    def _start(self):
        self.timer_logic.start()
        self.timer.move(10, 50)

        self.start_button.setVisible(False)
        self.stop_button.setVisible(True)

