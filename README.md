# 🖱️ COTTER — Clicker & Tracking Bot

Bot de détection d'image et de clic automatique (Windows) — projet éducatif, rapide et configurable.  
COTTER détecte une image modèle à l'écran, choisit la cible la plus proche (tracking) et clique automatiquement.

## Fonctionnalités

- Détection d'image en temps réel avec OpenCV
- Tracking intelligent : clique la cible la plus proche de la dernière cible ou du centre
- Latence optimisée via le paramètre `DELAY` et redimensionnement pour accélérer le matching
- Menu interactif dans le terminal pour configurer les touches (Pause/Resume, Quitter)
- Interface terminal centrée avec ASCII art

## Fichiers importants

| Fichier | Description |
|---|---|
| `bot.py` | Script principal |
| `install.bat` | Installe les dépendances requises (Windows) |
| `start.bat` | Lance le bot |
| `bot.bat` | Script d'aide / lancement (optionnel) |
| `assets/1.png` | Image modèle que le bot cherche (à remplacer selon votre usage) |

## Prérequis

- Windows (testé)
- Python 3.8+
- Modules Python : `opencv-python`, `numpy`, `pyautogui`, `pillow`, `pynput`

## Installation

```bash
git clone https://github.com/thedevnoxa/cotter
cd cotter
.\install.bat
```

Ou manuellement :

```bash
python -m pip install --upgrade pip
pip install opencv-python numpy pyautogui pillow pynput
```

## Utilisation

```bash
# Via le script d'assistance
.\start.bat

# Ou directement
python bot.py
```

## Menu et configuration

Au démarrage, le menu s'affiche centré dans le terminal. Vous pouvez :

- Lancer le bot
- Changer la touche Pause/Reprise
- Changer la touche Quitter
- Voir les touches actuelles

## ⚠️ Avertissement légal

Cet outil est destiné à un usage **éducatif uniquement**.  
Ne l'utilisez que sur des environnements dont vous avez l'autorisation explicite.  
L'utilisation non autorisée peut enfreindre les conditions d'utilisation des logiciels concernés.

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)

---
*Projet réalisé par [Noxa](https://github.com/thedevnoxa)*
