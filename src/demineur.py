"""Module providing Random variable generators."""
import random

class Demineur:
    """Class representing a Deminer game"""

    def __init__(self, nombre_mines=10):
        self.taille = 10
        self.nombre_mines = nombre_mines
        self.grille = [['.' for _ in range(self.taille)] for _ in range(self.taille)]
        self.grille_visible = [['.' for _ in range(self.taille)] for _ in range(self.taille)]
        self.__placer_mines()
        self.__calculer_indices()

    def __placer_mines(self):
        mines_placees = 0
        while mines_placees < self.nombre_mines:
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
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
        while True:
            self.afficher_grille()
            x, y = map(int, input("Entrez les coordonnees x et y separees par un espace: ").split())
            if self.grille[y][x] == 'M':
                print("Perdu !")

            self.decouvrir_cases(x, y)
            if sum(row.count('.') for row in self.grille_visible) == self.nombre_mines:
                print("Gagne !")


if __name__ == "__main__":
    jeu = Demineur()
    jeu.jouer()
