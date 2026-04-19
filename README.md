🤖 COTTER — Clicker & Tracking BotBot de détection d'image et de clic automatique pour Windows, conçu pour être rapide, léger et entièrement configurable.FonctionnalitésDétection d'image haute performance via OpenCV (Template Matching).Algorithme de Tracking : Cible intelligemment l'élément le plus proche du centre ou de la dernière position.Latence optimisée : Paramètre DELAY ajustable et redimensionnement dynamique pour maximiser les FPS.Menu Interactif : Interface terminal centrée avec ASCII art pour configurer vos touches à la volée.Contrôles à distance : Raccourcis clavier pour mettre en pause, reprendre ou quitter instantanément.InstallationBash# Cloner le dépôt
git clone https://github.com/thedevnoxa/cotter
cd cotter

# Installation automatique des dépendances (Windows)
.\install.bat
Note : Si vous préférez l'installation manuelle :Bashpython -m pip install --upgrade pip
pip install opencv-python numpy pyautogui pillow pynput
UtilisationPour lancer le bot, utilisez le lanceur ou la commande Python :PowerShell# Via le script d'assistance
.\start.bat

# Directement via Python
python bot.py
Configuration des touchesAu démarrage, un menu s'affiche dans le terminal. Vous pouvez configurer :Pause/Reprise (Par défaut : p)Quitter (Par défaut : $)Le prompt de sélection est centré et commence par :>.Structure du Projetbot.py : Script principal (Logique de détection + UI).install.bat : Installe l'environnement Python requis.start.bat / bot.bat : Scripts de lancement rapide.assets/1.png : Image modèle que le bot recherche à l'écran.Optimisation & TuningParamètreDescriptionConseilDELAYFréquence de scan0.001 (rapide) à 0.05 (éco).THRESHOLDPrécision du matchingEntre 0.6 (souple) et 0.9 (strict).PermissionsDroits d'accèsLancer en Admin si l'app ciblée est en Admin.⚠️ Avertissement légalCet outil est destiné à un usage éducatif uniquement.L'automatisation peut violer les conditions d'utilisation de certaines applications. Vous êtes responsable de l'usage que vous faites de ce logiciel.StackProjet réalisé par Noxa — Bac Pro CIEL
