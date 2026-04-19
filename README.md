# 🤖 COTTER — Clicker & Tracking Bot

Scanner de détection d'image et clic automatique (Windows) conçu pour être rapide, léger et entièrement configurable. Projet réalisé dans le cadre du Bac Pro CIEL.

## Fonctionnalités

- **Détection d'image haute performance** via OpenCV (Template Matching).
- **Algorithme de Tracking** : Cible intelligemment l'élément le plus proche du centre ou de la dernière position connue.
- **Latence optimisée** : Paramètre `DELAY` ajustable et redimensionnement dynamique pour maximiser les performances CPU.
- **Menu Interactif** : Interface terminal centrée avec ASCII art pour configurer vos touches à la volée.
- **Contrôles à distance** : Raccourcis clavier globaux pour mettre en pause, reprendre ou quitter instantanément.

## Installation

```bash
# Cloner le dépôt
git clone [https://github.com/thedevnoxa/cotter](https://github.com/thedevnoxa/cotter)
cd cotter

# Installation automatique des dépendances (Windows)
.\install.bat
