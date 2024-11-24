"""Module providing Random variable generators."""
import random
import json
import os
from statistiques import Statistiques
from colorama import init, Fore, Style

# Initialize colorama for colors
init()

class Demineur:
    """Class representing a Deminer game"""


    def __init__(self, fichier_sauvegarde='demineur.json', difficulte='moyen'):
        """
        Initialize the game with a grid and place mines based on difficulty level.

        :param difficulte: Difficulty level of the game ('facile', 'moyen', 'difficile').
        :raises ValueError: If the difficulty level is not one of 'facile', 'moyen', or 'difficile'.
        """
        if difficulte not in ['facile', 'moyen', 'difficile']:
            raise ValueError("Le niveau de difficulté doit être 'facile', 'moyen' ou 'difficile'.")
        if difficulte == 'facile':
            self.taille = 8
            self.nombre_mines = 10
        elif difficulte == 'difficile':
            self.taille = 16
            self.nombre_mines = 40
        else:  # moyen
            self.taille = 10
            self.nombre_mines = 20

        self.grille = [['■' for _ in range(self.taille)] for _ in range(self.taille)]
        self.grille_visible = [['■' for _ in range(self.taille)] for _ in range(self.taille)]
        self.statistiques = Statistiques()
        self.fichier_sauvegarde = fichier_sauvegarde
        self.marques = set()
        self.__placer_mines()
        self.__calculer_indices()

    def __placer_mines(self):
        mines_placees = 0
        while mines_placees < self.nombre_mines:
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
            if self.grille[y][x] != 'M':
                self.grille[y][x] = 'M'
                mines_placees += 1

    def __calculer_indices(self):
        for y in range(self.taille):
            for x in range(self.taille):
                if self.grille[y][x] == 'M':
                    continue
                mines_autour = 0
                for dx in range(y - 1, y + 2):
                    for dy in range(x - 1, x + 2):
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= self.taille or ny >= self.taille:
                            continue
                        if self.grille[ny][nx] == 'M':
                            mines_autour += 1
                self.grille[y][x] = str(mines_autour)

    def decouvrir_cases(self, x, y):
        """A Function to uncover a cell"""
        # Vérifier si les coordonnées sont dans les limites de la grille
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return
        if self.grille_visible[y][x] == 'F':
            self.grille_visible[y][x] = self.grille[y][x]
        if self.grille_visible[y][x] != '■':
            return
        self.grille_visible[y][x] = self.grille[y][x]
        if self.grille[y][x] == '0':
            self.decouvrir_cases(x - 1, y)
            self.decouvrir_cases(x + 1, y)
            self.decouvrir_cases(x, y - 1)
            self.decouvrir_cases(x, y + 1)

    def afficher_grille(self):
        """A Function to show the game's board"""
        print("    "+ " ".join([str(i) for i in range(self.taille)]))
        for idx, ligne in enumerate(self.grille_visible):
            print(f"{idx:2}| " + ' '.join(ligne) + " |")

    def charger_jeu(self):
        """
        Load the game state from a JSON file.
        """
        if os.path.exists(self.fichier_sauvegarde):
            with open(self.fichier_sauvegarde, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.taille = data.get('taille', 10)
                self.nombre_mines = data.get('nombre_mines', 10)
                self.grille = data.get(
                    'grille', [['.' for _ in range(self.taille)] for _ in range(self.taille)]
                )
                self.grille_visible = data.get(
                    'grille_visible', 
                    [['.' for _ in range(self.taille)] for _ in range(self.taille)]
                )
    def marquer_case(self, x, y):
        """ Mark or unmark a cell with a flag. """
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return
        if self.grille_visible[y][x] == 'F':
            self.grille_visible[y][x] = '.'
        elif self.grille_visible[y][x] == '.':
            self.grille_visible[y][x] = 'F'
        else:
            print("La case est déjà découverte et ne peut pas être marquée.")

    def sauvegarder_jeu(self):
        """
        Save the current game state to a JSON file.
        """
        data = {
            'taille': self.taille,
            'nombre_mines': self.nombre_mines,
            'grille': self.grille,
            'grille_visible': self.grille_visible,
        }
        with open(self.fichier_sauvegarde, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Jeu sauvegardé dans {self.fichier_sauvegarde}.")

    def afficher_instructions(self):
        """Affiche les instructions du jeu"""
        print(f"\n{Fore.CYAN}=== COMMANDES DISPONIBLES ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}• x y{Style.RESET_ALL}     : Découvrir la case aux coordonnées (x,y)")
        print(f"{Fore.WHITE}• f x y{Style.RESET_ALL}   : Marquer/Démarquer une case avec un drapeau")
        print(f"{Fore.WHITE}• save{Style.RESET_ALL}    : Sauvegarder la partie")
        print(f"{Fore.WHITE}• quit{Style.RESET_ALL}    : Quitter la partie")
        print("\n" + "─" * 40)

    def jouer(self):
        """A Function to launch the game."""
        game_in_progress = True
        self.statistiques.start_timer()
        self.afficher_instructions()  # Afficher les instructions au début

        while game_in_progress:
            print(f"\n{Fore.CYAN}[ Bienvenue au Démineur ! ]{Style.RESET_ALL}\n")
            self.afficher_grille()
            print(f"\n{Fore.GREEN}Entrez une commande >{Style.RESET_ALL} ", end='')
            choix = input().strip().split()

            if not choix:
                continue

            if choix[0].lower() == 'save':
                self.sauvegarder_jeu()
                continue
            elif choix[0].lower() == 'quit':
                if input(f"{Fore.YELLOW}Voulez-vous vraiment quitter ? (o/n): {Style.RESET_ALL}").lower() == 'o':
                    print("Partie terminée !")
                    break
                continue

            try:
                if len(choix) == 3 and choix[0] == 'f':
                    x, y = map(int, choix[1:])
                    self.marquer_case(x, y)
                    continue
                if len(choix) == 2:
                    x, y = map(int, choix)
                else:
                    print(f"{Fore.RED}Erreur : entrez 'f x y' pour marquer/démarquer, ou 'x y' pour découvrir.{Style.RESET_ALL}")
                    continue
            except ValueError:
                print(f"{Fore.RED}Coordonnées invalides. Veuillez réessayer.{Style.RESET_ALL}")
                continue

            if self.grille[y][x] == 'M':
                self.decouvrir_cases(x, y)
                self.afficher_grille()
                print(f"\n{Fore.RED}💥 BOOM ! Partie perdue ! 💥{Style.RESET_ALL}")
                game_in_progress = False
                temps_ecoule = self.statistiques.stop_timer()
                self.statistiques.record_loss()
                break

            self.decouvrir_cases(x, y)
            if sum(row.count('■') for row in self.grille_visible) == self.nombre_mines:
                print(f"\n{Fore.GREEN}🎉 VICTOIRE ! Félicitations ! 🎉{Style.RESET_ALL}")
                game_in_progress = False
                temps_ecoule = self.statistiques.stop_timer()
                self.statistiques.record_victory()
                break

        print(f"\nTemps écoulé : {temps_ecoule:.2f} secondes")
        self.statistiques.display_statistics()

        while True:
            restart = input(f"\n{Fore.CYAN}Voulez-vous recommencer une partie ? (oui/non) : {Style.RESET_ALL}").lower()
            if restart == 'oui':
                nouveau_jeu = Demineur(self.nombre_mines)
                nouveau_jeu.jouer()
                break
            if restart == 'non':
                print(f"\n{Fore.YELLOW}Merci d'avoir joué ! Au revoir !{Style.RESET_ALL}")
                break
            print(f"{Fore.RED}Réponse invalide, veuillez répondre par 'oui' ou 'non'.{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.CYAN}=== DÉMINEUR ==={Style.RESET_ALL}")
    niveau_difficulte = input("Choisissez un niveau de difficulté (facile, moyen, difficile): ")
    try:
        jeu = Demineur(niveau_difficulte)
        jeu.charger_jeu()
        jeu.jouer()
    except ValueError as e:
        print(f"{Fore.RED}{str(e)}{Style.RESET_ALL}")