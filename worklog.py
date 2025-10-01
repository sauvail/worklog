import keyboard
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import subprocess
import sys
import time
import pygetwindow as gw

FILE_PATH = os.path.join(os.path.expanduser("~"), "worklog.txt")

def log_text():
    root = tk.Tk()
    root.title("")
    root.geometry("300x50")
    root.attributes('-topmost', True)
    root.resizable(False, False)
    root.configure(bg="white")
    root.lift()
    root.focus_force()

    entry = tk.Entry(root, width=45, bd=1, relief="solid", font=("Arial", 10))
    entry.pack(padx=5, pady=5)
    entry.focus_set()

    def save_and_close(event=None):
        text = entry.get().strip()
        if text:
            now = datetime.now()
            timestamp = now.strftime("%H:%M") + " | "
            date_str = now.strftime("%d/%m/%Y")
            if not os.path.exists(FILE_PATH):
                with open(FILE_PATH, "w", encoding="utf-8") as f:
                    f.write("")
            need_date_header = True
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                if f"----- {date_str} -----" in f.read():
                    need_date_header = False
            with open(FILE_PATH, "a", encoding="utf-8") as f:
                if need_date_header:
                    f.write(f"\n----- {date_str} -----\n")
                f.write(f"{timestamp} {text}\n")
        root.destroy()

    def cancel(event=None):
        root.destroy()

    entry.bind("<Return>", save_and_close)
    entry.bind("<Escape>", cancel)
    root.mainloop()

def open_worklog():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write("")
    subprocess.Popen(["notepad.exe", FILE_PATH])
    time.sleep(0.2)
    windows = gw.getWindowsWithTitle("worklog.txt - Notepad")
    if windows:
        windows[0].activate()

def exit_program():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.focus_force()
    if messagebox.askyesno("Quit Worklog", "Do you really want to quit?", parent=root):
        root.destroy()
        keyboard.unhook_all()  # désactive tous les hotkeys
        os._exit(0)  # FORCE la fermeture du processus
    else:
        root.destroy()

# Raccourcis globaux
keyboard.add_hotkey("ctrl+shift+f1", log_text)
keyboard.add_hotkey("ctrl+shift+f2", open_worklog)
keyboard.add_hotkey("ctrl+shift+f3", exit_program)

print("Worklog running...")
print(" - Ctrl+Shift+F1 : Add a note")
print(" - Ctrl+Shift+F2 : Open worklog.txt (focus)")
print(" - Ctrl+Shift+F3 : Quit program")
print(" - Escape (in textbox) : close without saving")

# Loop minimal pour maintenir le script actif
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    keyboard.unhook_all()
