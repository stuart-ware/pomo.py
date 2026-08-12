from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QLabel, QWidget

from pomo.var import FONT, PROGRAM_VERSION


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(f"pomo.py {PROGRAM_VERSION}")
        self.program_font: QtGui.QFont = QtGui.QFont(FONT, 10)
        self.setFixedSize(QtCore.QSize(200,200))
        
        # Labels

        self.program_name: QLabel = QLabel("pomo.py 0.3.0", self)
        self.program_name.setFont(QtGui.QFont(FONT, 8))
        self.program_name.move(56, 180)



