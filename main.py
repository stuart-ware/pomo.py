from timer import Timer
import tkinter as tk
import os

if __name__ == "__main__":

    def update_label(time_str):
        timer_label.config(text=time_str)

    def timer_done():
        timer_label.config(text="Done!")
        done = 'notify-send "pomo.py" "Done!"'
        os.system(done)

    def start_pomo():
        pomo = Timer(25, update_label, timer_done, window)
        pomo.start()
        focus = 'notify-send "pomo.py" "Its time to focus!"'
        os.system(focus)

    def start_rest():
        pomo = Timer(5, update_label, timer_done, window)
        pomo.start()
        rest = 'notify-send "pomo.py" "Its time to rest"'
        os.system(rest)

    window = tk.Tk()
    window.title("pomo.py")
    window.geometry("300x300")
    window.resizable(False, False)

    timer_label = tk.Label(window, text="pomo.py", font=(
        "JetBrains Mono Nerd Font", 45))
    timer_label.pack(pady=80)

    start_button = tk.Button(window, text="Start", command=start_pomo)
    start_button.pack()
    start_button.place(x=95, y=260)

    rest_button = tk.Button(window, text="Rest", command=start_rest)
    rest_button.pack()
    rest_button.place(x=155, y=260)

    window.mainloop()
