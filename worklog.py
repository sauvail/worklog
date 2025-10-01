import keyboard
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import subprocess
import sys

# Chemin dynamique pour le fichier worklog
FILE_PATH = os.path.join(os.path.expanduser("~"), "worklog.txt")

def log_text():
    """Ouvre une petite fenêtre pour saisir une note et l'ajoute au fichier."""
    root = tk.Tk()
    root.title("")
    root.geometry("300x50")
    root.attributes('-topmost', True)
    root.resizable(False, False)
    root.configure(bg="white")

    # Force la fenêtre au premier plan et focus
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

            # Crée le fichier s'il n'existe pas
            if not os.path.exists(FILE_PATH):
                with open(FILE_PATH, "w", encoding="utf-8") as f:
                    f.write("")

            # Vérifie si l'en-tête de la date existe déjà
            need_date_header = True
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                if f"----- {date_str} -----" in f.read():
                    need_date_header = False

            # Écrit dans le fichier
            with open(FILE_PATH, "a", encoding="utf-8") as f:
                if need_date_header:
                    f.write(f"\n----- {date_str} -----\n")
                f.write(f"{timestamp} {text}\n")

        root.destroy()

    # Fermer la fenêtre si Escape est pressé
    def cancel(event=None):
        root.destroy()

    entry.bind("<Return>", save_and_close)
    entry.bind("<Escape>", cancel)
    root.mainloop()

def open_worklog():
    """Ouvre le fichier worklog.txt dans le Bloc-notes."""
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write("")
    subprocess.Popen(["notepad.exe", FILE_PATH])

def exit_program():
    """Ferme le programme avec confirmation, fenêtre forcée au focus et arrêt propre."""
    # Crée une fenêtre invisible pour parent du messagebox
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.focus_force()

    if messagebox.askyesno("Quitter Worklog", "Voulez-vous vraiment quitter le Worklog ?", parent=root):
        root.destroy()
        keyboard.unhook_all()  # désactive tous les hotkeys
        sys.exit()
    root.destroy()

# Raccourcis globaux
keyboard.add_hotkey("ctrl+shift+f1", log_text)
keyboard.add_hotkey("ctrl+shift+f2", open_worklog)
keyboard.add_hotkey("ctrl+shift+f3", exit_program)

print("Worklog en cours d'exécution...")
print(" - Ctrl+Maj+F1 : Ajouter une note")
print(" - Ctrl+Maj+F2 : Ouvrir le fichier worklog")
print(" - Ctrl+Maj+F3 : Quitter le programme")
print(" - Échap (dans la textbox) : fermer sans enregistrer")
keyboard.wait()
