Documentation démineur
======================

Ceci est la documentation du démineur.

.. grid:: 2

    .. grid-item-card::  API reference
        :link: api
        :link-type: doc

        Cette section contient la description des fonctions du demineur.
        Elle décrit comment les méthodes fonctionnent et les paramètres peuvent être utilisés.

Introduction
------------

Le Démineur est un jeu classique de stratégie et de réflexion. Le but est de révéler toutes les cases d'une grille sans déclencher de mine.
Le joueur utilise des indices numériques pour déduire l'emplacement des mines.

Fonctionnalités principales
---------------------------

1. **Initialisation de la grille** :
   Le jeu génère une grille en fonction du niveau de difficulté choisi :
   - Facile : Grille 8x8 avec 10 mines.
   - Moyen : Grille 10x10 avec 20 mines.
   - Difficile : Grille 16x16 avec 40 mines.

2. **Placement des mines** :
   Les mines sont placées aléatoirement au début de chaque partie.

3. **Calcul des indices** :
   Chaque case affiche un chiffre indiquant le nombre de mines adjacentes.

4. **Découverte des cases** :
   - Les cases sans mine ou chiffre déclenchent une cascade de révélations.
   - Une case contenant une mine entraîne une défaite.

5. **Marquage des cases suspectes** :
   Le joueur peut placer ou retirer des drapeaux pour indiquer les cases suspectées d'être des mines.

6. **Affichage de la grille** :
   La grille visible est constamment mise à jour et affichée avec :
   - Les cases découvertes,
   - Les drapeaux,
   - Le nombre de mines restantes,
   - Le temps écoulé et le nombre de mouvements effectués.

7. **Sauvegarde et reprise** :
   L'état du jeu peut être sauvegardé dans un fichier JSON pour être repris ultérieurement.

8. **Statistiques de performance** :
   Le jeu suit les performances du joueur :
   - Nombre de victoires et défaites,
   - Temps de jeu total et moyen,
   - Nombre de parties jouées.

9. **Gestion des niveaux de difficulté** :
   Le joueur peut choisir entre trois niveaux de difficulté :
   - Facile : Une grille petite avec peu de mines, idéale pour les débutants.
   - Moyen : Une grille intermédiaire pour les joueurs habitués.
   - Difficile : Une grande grille remplie de mines pour les experts.

10. **Rejouer ou quitter** :
    À la fin d'une partie, le joueur peut choisir de rejouer ou de quitter. Cela permet de recommencer une nouvelle session de jeu.

Glossaire
---------

- **Mine** : Une case qui, si découverte, met fin à la partie.
- **Indice** : Un chiffre sur une case indiquant le nombre de mines adjacentes.
- **Cascade** : Révélation automatique des cases vides adjacentes à une case vide découverte.
- **Grille** : Plateau de jeu contenant les cases et les mines.
- **Drapeau** : Un marqueur utilisé pour signaler une case suspectée d'abriter une mine.
- **Niveaux de difficulté** : Paramètre permettant de personnaliser la taille de la grille et le nombre de mines.

.. toctree::
    :hidden:

    api
