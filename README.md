# Worklog Shortcut Logger

A program to quickly add timestamped notes to a text file using global keyboard shortcuts.

---

## Features
- **Ctrl + Shift + F1**: Opens a small window to enter a note.  
  - The note is saved in `worklog.txt` in the current user's folder  
    (example: `C:\Users\YourName\worklog.txt`).  
  - The first message of each day is preceded by a header `----- dd/mm/yyyy -----`.  
  - The window is compact, minimal, and automatically receives **focus**.  
  - Press **Enter** to save the note.  
  - Press **Escape** to close the window without saving.  

- **Ctrl + Shift + F2**: Opens the `worklog.txt` file in Notepad.  

- **Ctrl + Shift + F3**: Closes the program with a confirmation dialog, properly stopping all background tasks.  

- The file is automatically created if it does not exist.

Example file:
```
----- 01/10/2025 -----
09:12 First note of the day
10:30 Another note
```

---

## Installation

1. Install [Python 3](https://www.python.org/downloads/windows/) on Windows.  
   During installation, check **"Add Python to PATH"**.

2. Install dependencies:
   ```bash
   pip install keyboard pygetwindow
   ```
   (`tkinter` is included by default with Python on Windows.)

3. Save the script as `worklog.py`.

4. Run:
   - With console visible:  
     ```bash
     python worklog.py
     ```
   - In the background (no console window):  
     ```bash
     pythonw worklog.py
     ```

---

## Creating an executable (.exe)

1. Install pyinstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --noconsole --onefile worklog.py
   ```

3. The final file will be in `dist/worklog.exe`.

---

## Auto-start on Windows

Copy `worklog.exe` to:
```
C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

The program will automatically start at the next Windows login.

---

## Shortcut keys

- **Ctrl + Shift + F1** → Add a note  
- **Ctrl + Shift + F2** → Open `worklog.txt`  
- **Ctrl + Shift + F3** → Quit the program with confirmation  
- **Escape (in the textbox)** → Close the textbox without saving
