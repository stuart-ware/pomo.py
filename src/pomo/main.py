import sys

from PySide6.QtWidgets import QApplication

from pomo.ui.window import Window

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())