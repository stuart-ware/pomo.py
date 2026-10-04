from PySide6.QtWidgets import QApplication
from pomo_py import pomo    
import sys

def main():
    app = QApplication([])
    window = pomo.WindowCountdown()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
