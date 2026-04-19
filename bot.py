import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
import sys
import os
from pynput import keyboard

import shutil
# ═══════════════════════════════════════════════════════════
# ⚙️  CONFIGURATION DES TOUCHES - À MODIFIER ICI
# ═══════════════════════════════════════════════════════════
KEY_TOGGLE = 'p'      # Pause/Reprise du bot
KEY_EXIT = '$'        # Quitter le programme
# ═══════════════════════════════════════════════════════════

# Codes couleur ANSI
class Colors:
    BLUE1 = '\033[38;5;33m'      # Bleu clair
    BLUE2 = '\033[38;5;39m'      # Bleu
    BLUE3 = '\033[38;5;45m'      # Bleu-Cyan
    PURPLE1 = '\033[38;5;57m'    # Bleu-Violet
    PURPLE2 = '\033[38;5;63m'    # Violet
    PURPLE3 = '\033[38;5;99m'    # Violet foncé
    RESET = '\033[0m'
    BOLD = '\033[1m'


def get_ascii_art_lines():
    """Retourne l'ASCII art en couleur (liste de lignes)."""
    lines = [
        (Colors.BLUE2, "        ██████╗ ██████╗ ████████╗███████╗███╗"),
        (Colors.BLUE3, "       ██╔════╝██╔═══██╗╚══██╔══╝██╔════╝████╗"),
        (Colors.PURPLE1, "       ██║     ██║   ██║   ██║   █████╗  ██╔██╗"),
        (Colors.PURPLE2, "       ██║     ██║   ██║   ██║   ██╔══╝  ██║ ██╗"),
        (Colors.PURPLE2, "       ╚██████╗╚██████╔╝   ██║   ███████╗██║  ██╗"),
        (Colors.PURPLE3, "        ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝"),
        (Colors.PURPLE1, "            ULTRA-RAPIDE + TRACKING"),
    ]
    # Convert to colored strings
    return [f"{c}{s}{Colors.RESET}" for c, s in lines]


def print_centered_lines(lines, term_cols):
    """Affiche une liste de lignes centrées horizontalement selon term_cols."""
    for ln in lines:
        try:
            import re
            visible = re.sub(r'\x1b\[[0-9;]*m', '', ln)
            pad = max(0, (term_cols - len(visible)) // 2)
            print(' ' * pad + ln)
        except Exception:
            print(ln)


def centered_input(prompt_text, cols):
    """Affiche un prompt centré et retourne la saisie utilisateur."""
    pad = max(0, (cols - len(prompt_text)) // 2)
    return input(' ' * pad + prompt_text)


def centered_print(text, cols, delay=0):
    pad = max(0, (cols - len(text)) // 2)
    print(' ' * pad + text)
    if delay > 0:
        time.sleep(delay)

class ImageClickerBot:
    def __init__(self, template_path, threshold=0.7, delay=0.001, key_toggle='p', key_exit='$'):
        """Bot ultra-optimisé avec tracking"""
        self.template = cv2.imread(template_path)
        if self.template is None:
            raise ValueError(f"Image non trouvée: {template_path}")
        
        # Redimensionner le template pour accélérer la détection
        self.template_gray = cv2.cvtColor(self.template, cv2.COLOR_BGR2GRAY)
        self.template_small = cv2.resize(self.template_gray, (0, 0), fx=0.5, fy=0.5)
        self.template_h, self.template_w = self.template_small.shape
        self.threshold = threshold
        self.delay = delay
        self.running = False
        self.active = True
        self.last_pos = None  # Position de la dernière cible cliquée
        
        # Configurer les touches
        self.key_toggle = key_toggle.lower()
        self.key_exit = key_exit.lower()
        
        # Obtenir la résolution écran (pixels)
        screenshot = np.array(ImageGrab.grab())
        self.screen_h, self.screen_w = screenshot.shape[:2]
        self.center_x = self.screen_w // 2
        self.center_y = self.screen_h // 2
        
        print(f"✓ Bot mode ultra-rapide + Tracking activé")
        print(f"CONTRÔLES: [{self.key_toggle.upper()}] Pause/Reprise | [{self.key_exit}] Quitter\n")
    
    def capture_screen_fast(self):
        """Capture rapide + redimensionnement"""
        screenshot = np.array(ImageGrab.grab())
        screenshot_bgr = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        # Redimensionner pour accélérer le matching
        return cv2.resize(screenshot_bgr, (0, 0), fx=0.5, fy=0.5)
    
    def find_all_targets(self, screenshot):
        """Trouve les targets - optimisé rapidité"""
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot_gray, self.template_small, cv2.TM_CCOEFF_NORMED)
        
        # Limiter à 5 meilleurs matches pour éviter overhead
        locations = np.where(result >= self.threshold)
        matches = []
        
        for pt in zip(*locations[::-1]):
            confidence = result[pt[1], pt[0]]
            matches.append((pt[0], pt[1], confidence))
        
        # Trier par confiance et garder que les top 5
        matches = sorted(matches, key=lambda m: m[2], reverse=True)[:5]
        
        # Convertir coordonnées
        return [(m[0] * 2 + self.template_w, m[1] * 2 + self.template_h, m[2]) for m in matches]
    
    def calculate_distance(self, x, y):
        """Distance ultra-rapide"""
        if self.last_pos:
            dx = x - self.last_pos[0]
            dy = y - self.last_pos[1]
            return dx * dx + dy * dy  # Pas de sqrt = plus rapide
        return (x - self.center_x) ** 2 + (y - self.center_y) ** 2
    
    def find_closest_target(self, targets):
        """Trouve la plus proche - O(n) minimal"""
        if not targets:
            return None
        return min(targets, key=lambda t: self.calculate_distance(t[0], t[1]))
    
    def move_and_click(self, x, y):
        """Clic direct"""
        pyautogui.click(x, y)
        self.last_pos = (x, y)  # Mémoriser la position
    
    def toggle_running(self):
        """Active/Désactive"""
        self.running = not self.running
        print(f"Bot {'ON' if self.running else 'OFF'}")
    
    def stop(self):
        """Arrête"""
        self.active = False
    
    def run(self):
        """Boucle ultra-optimisée avec tracking"""
        try:
            while self.active:
                if self.running:
                    screenshot = self.capture_screen_fast()
                    targets = self.find_all_targets(screenshot)
                    
                    if targets:
                        closest = self.find_closest_target(targets)
                        if closest:
                            x, y, confidence = closest
                            self.move_and_click(x, y)
                    
                    time.sleep(0.001)
                else:
                    time.sleep(0.001)
        except Exception as e:
            print(f"Erreur: {e}")


def on_press(key, bot):
    """Gère les touches pressées"""
    try:
        if hasattr(key, 'char'):
            char = key.char.lower() if key.char else ''
            if char == bot.key_toggle:
                bot.toggle_running()
            elif char == bot.key_exit:
                bot.stop()
                return False  # Arrête le listener
    except AttributeError:
        pass


def show_menu():
    """Affiche le menu de configuration centré dans le terminal"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        term = shutil.get_terminal_size()
        cols, lines = term.columns, term.lines

        ascii_lines = get_ascii_art_lines()
        menu_lines = [
            "MENU PRINCIPAL",
            "",
            "1. Lancer le bot",
            "2. Changer la touche Pause/Reprise",
            "3. Changer la touche Quitter",
            "4. Afficher les touches actuelles",
            "5. Quitter",
            "",
        ]

        total_lines = len(ascii_lines) + len(menu_lines)
        top_padding = max(0, (lines - total_lines) // 2)
        print('\n' * top_padding, end='')

        # imprimer ascii centré horizontalement
        print_centered_lines(ascii_lines, cols)
        print()

        # imprimer menu centré horizontalement
        for ml in menu_lines:
            pad = max(0, (cols - len(ml)) // 2)
            print(' ' * pad + ml)

        # Prompt centré avec préfixe ':>'
        prompt = ':> '
        choice = centered_input('\n' + prompt, cols).strip()

        # Reset écran et afficher confirmation centrée
        os.system('cls' if os.name == 'nt' else 'clear')
        centered_print(f":> Option {choice} sélectionnée", cols, delay=0.35)

        if choice == '1':
            return 'start'
        elif choice == '2':
            new_key = centered_input('\nNouvelle touche Pause/Reprise (ex: p, space, r): ', cols).strip().lower()
            if new_key:
                globals()['KEY_TOGGLE'] = new_key
                os.system('cls' if os.name == 'nt' else 'clear')
                centered_print(f":> Touche changée en: {new_key.upper()}", cols)
                input('\nAppuyez sur Entrée pour revenir au menu...')
        elif choice == '3':
            new_key = centered_input('\nNouvelle touche Quitter (ex: $, q, esc): ', cols).strip()
            if new_key:
                globals()['KEY_EXIT'] = new_key
                os.system('cls' if os.name == 'nt' else 'clear')
                centered_print(f":> Touche changée en: {new_key}", cols)
                input('\nAppuyez sur Entrée pour revenir au menu...')
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            centered_print('Touches actuelles:', cols)
            centered_print(f"Pause/Reprise: [{KEY_TOGGLE.upper()}]", cols)
            centered_print(f"Quitter:       [{KEY_EXIT}]", cols)
            input('\nAppuyez sur Entrée pour revenir au menu...')
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            centered_print('Au revoir!', cols)
            sys.exit(0)
        else:
            print("Option invalide!")
            time.sleep(1)


def start_bot():
    """Lance le bot avec les touches configurées"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(script_dir, "assets", "1.png")
    
    if not os.path.exists(IMAGE_PATH):
        print(f"❌ Erreur: Image non trouvée à l'emplacement: {IMAGE_PATH}")
        sys.exit(1)
    
    term = shutil.get_terminal_size()
    print_centered_lines(get_ascii_art_lines(), term.columns)
    
    try:
        bot = ImageClickerBot(IMAGE_PATH, 0.7, 0.001, KEY_TOGGLE, KEY_EXIT)
        
        listener = keyboard.Listener(on_press=lambda key: on_press(key, bot))
        listener.start()
        
        bot.run()
        
        listener.stop()
        
    except ValueError as e:
        print(f"❌ Erreur: {e}")
    except Exception as e:
        print(f"❌ Erreur: {e}")


def main():
    """Point d'entrée - affiche le menu"""
    menu_choice = show_menu()
    
    if menu_choice == 'start':
        start_bot()


if __name__ == "__main__":
    print("Démarrage dans 1 secondes...")
    time.sleep(1)
    main()
