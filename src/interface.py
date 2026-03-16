import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import time
import threading

class AutomationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Automation Interface")

        # Buttons
        self.start_button = tk.Button(master, text="Start", width=15, command=self.start_script)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", width=15, command=self.stop_script, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Timer label
        self.timer_label = tk.Label(master, text="Elapsed Time: 00:00:00", font=("Arial", 12))
        self.timer_label.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(master, text="Reset Timer", width=15, command=self.reset_timer)
        self.reset_button.pack(pady=5)

        # Process variables
        self.process = None
        self.running = False  # האם הסקריפט רץ

        # Timer variables
        self.elapsed_seconds = 0
        self.last_update_time = None

        # Start timer update loop
        self.update_timer()

    # Start subprocess
    def start_script(self):
        if self.process is None:
            # Path to game_automation.py
            script_path = os.path.join(os.path.dirname(__file__), "game_automation.py")

            # Run game_automation.py as unbuffered subprocess
            self.process = subprocess.Popen(
                [os.path.join("..", "venv", "Scripts", "python.exe"), "-u", script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8"
            )

            # Start a thread to read output
            threading.Thread(target=self.read_output_thread, daemon=True).start()

        # Enable timer
        self.running = True
        self.last_update_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    # Stop subprocess
    def stop_script(self):
        if self.process:
            self.process.terminate()
            self.process = None

        # Stop timer
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Stopped", "The script has been stopped successfully")

    # Reset timer
    def reset_timer(self):
        self.elapsed_seconds = 0
        self.last_update_time = time.time() if self.running else None
        self.timer_label.config(text="Elapsed Time: 00:00:00")

    # Timer update loop
    def update_timer(self):
        if self.running and self.last_update_time is not None:
            now = time.time()
            self.elapsed_seconds += int(now - self.last_update_time)
            self.last_update_time = now

        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        self.timer_label.config(text=f"Elapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d}")

        self.master.after(1000, self.update_timer)

    # Thread to read output from game_automation.py
    def read_output_thread(self):
        for line in self.process.stdout:
            print(line.strip())  # The output of game_automation.py goes directly to the IntelliJ console

# Run the GUI
root = tk.Tk()
app = AutomationGUI(root)
root.geometry("300x200")
root.mainloop()
