import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

app: QApplication = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)  # para que no se cierre al cerrar ventanas

tray: QSystemTrayIcon = QSystemTrayIcon(QIcon("logo.png"))
tray.setToolTip("Mi app")

menu = QMenu()
accion_salir = QAction("Salir")
accion_salir.triggered.connect(app.quit)
menu.addAction(accion_salir)

tray.setContextMenu(menu)
tray.show()
tray.showMessage(
                "Mi app",
                "Sigue corriendo en la bandeja del sistema",
                QSystemTrayIcon.Information,
                2000
            )
sys.exit(app.exec())