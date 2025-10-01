# Worklog Shortcut Logger

Programme permettant d’ajouter rapidement des notes horodatées dans un fichier texte via des raccourcis clavier globaux.

---

## Fonctionnalités
- **Ctrl + Maj + F1** : ouvre une petite fenêtre pour saisir une note.  
  - La note est enregistrée dans `worklog.txt` dans le dossier utilisateur courant  
    (exemple : `C:\Users\MonNom\worklog.txt`).  
  - Le premier message de chaque jour est précédé d’un en-tête `----- dd/mm/yyyy -----`.  
- **Ctrl + Maj + F2** : ouvre directement le fichier `worklog.txt` dans le Bloc-notes.  
- **Ctrl + Maj + F3** : ferme le programme avec une fenêtre de confirmation.  
- Le fichier est créé automatiquement s’il n’existe pas.

Exemple de fichier :
```
----- 01/10/2025 -----
09:12 Premier message du jour
10:30 Autre message
```

---

## Installation

1. Installer [Python 3](https://www.python.org/downloads/windows/) pour Windows.  
   Pendant l’installation, cocher **"Add Python to PATH"**.

2. Installer les dépendances :
   ```bash
   pip install keyboard
   ```
   (`tkinter` est inclus par défaut avec Python sur Windows.)

3. Sauvegarder le script sous `worklog.py`.

4. Lancer :
   - Avec console visible :  
     ```bash
     python worklog.py
     ```
   - En arrière-plan (sans fenêtre noire) :  
     ```bash
     pythonw worklog.py
     ```

---

## Génération d’un exécutable (.exe)

1. Installer pyinstaller :
   ```bash
   pip install pyinstaller
   ```

2. Créer l’exécutable :
   ```bash
   pyinstaller --noconsole --onefile worklog.py
   ```

3. Le fichier final se trouve dans `dist/worklog.exe`.

---

## Lancement automatique au démarrage

Copier `worklog.exe` dans le dossier :
```
C:\Users\<UTILISATEUR>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

Le programme se lancera automatiquement au prochain redémarrage de Windows.

---

## Récapitulatif des raccourcis
- **Ctrl + Maj + F1** → Ajouter une note  
- **Ctrl + Maj + F2** → Ouvrir le fichier `worklog.txt`  
- **Ctrl + Maj + F3** → Quitter le programme (avec confirmation)
