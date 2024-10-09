"""Module providing Random variable generators."""
import random

class Demineur:
    """Class representing a Deminer game"""

    def __init__(self, difficulte='moyen'):
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

        self.grille = [['.' for _ in range(self.taille)] for _ in range(self.taille)]
        self.grille_visible = [['.' for _ in range(self.taille)] for _ in range(self.taille)]
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
        if self.grille_visible[y][x] != '.':
            return

        self.grille_visible[y][x] = self.grille[y][x]

        if self.grille[y][x] == '0':
            self.decouvrir_cases(x - 1, y)
            self.decouvrir_cases(x + 1, y)
            self.decouvrir_cases(x, y - 1)
            self.decouvrir_cases(x, y + 1)

    def afficher_grille(self):
        """A Function to show the game's board"""
        for ligne in self.grille_visible:
            print(' '.join(ligne))

    def jouer(self):
        """A Function to launch the game"""

        game_in_progress = True
        while game_in_progress:
            self.afficher_grille()
            x, y = map(int, input("Entrez les coordonnees x et y separees par un espace: ").split())
            if self.grille[y][x] == 'M':
                #Display the grid with the mine visible
                self.decouvrir_cases(x, y)
                self.afficher_grille()
                print("Perdu !")
                #End the game
                game_in_progress = False
            self.decouvrir_cases(x, y)
            if sum(row.count('.') for row in self.grille_visible) == self.nombre_mines:
                print("Gagne !")
                #End the game
                game_in_progress = False


if __name__ == "__main__":
    niveau_difficulte = input("Choisissez un niveau de difficulte (facile, moyen, difficile): ")
    try:
        jeu = Demineur(niveau_difficulte)
        jeu.jouer()
    except ValueError as e:
        print(e)
