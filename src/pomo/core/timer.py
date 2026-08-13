from typing import Final

from PySide6 import QtCore


class Timer(QtCore.QObject):
    tick: Final = QtCore.Signal(int, int)

    def __init__(self) -> None:

        super().__init__()
        self.minutes: int = 0
        self.seconds: int = 0
        
        self.timer: Final = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.connection: Final = self.timer.timeout.connect(self._update_timer)

    def start(self):
        self.minutes = 1
        self.seconds = 0
        self.timer.start()
        self._update_timer()

    def stop(self):
        self.minutes = 0
        self.seconds = 0
        self.tick.emit(self.minutes, self.seconds)      

    def _update_timer(self) -> None:
        if self.seconds == 0: 
            if self.minutes == 0:
                self.stop()
                return
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1

        self.tick.emit(self.minutes, self.seconds)