# Class Timer

class Timer:
    def __init__(self, minutes, update, finish, tk_root):
        self.remaining = minutes * 60  # Minutes
        self.update = update
        self.finish = finish
        self.root = tk_root

    def start(self):
        self._tick()

    def _tick(self):
        mins, secs = divmod(self.remaining, 60)
        self.update(f"{mins:02}:{secs:02}")

        if self.remaining > 0:
            self.remaining -= 1
            self.root.after(1000, self._tick)
        else:
            self.finish()
