from src.game_engine.board import Board
from src.players.player import BasePlayer


class GameEngine:
    """
    Classe utilisée pour modéliser et gérer une partie de Dames.

        Attributs :
            joueur_blanc (Joueur) : Le premier joueur.
            joueur_noir (joueur) : Le deuxième joueur.
            joueur_courant (int) : Un entier représentant le joueur courant.

        Interface :
            change_joueur() : Change le joueur courant.
            run() : Fonction principale permettant de joueur une partie.
    """
    def __init__(self, joueur_blanc: BasePlayer, joueur_noir: BasePlayer):
        self.joueur_blanc = joueur_blanc
        self.joueur_noir = joueur_noir
        self.joueur_courant = joueur_blanc

    def change_joueur(self):
        if self.joueur_courant == self.joueur_blanc:
            self.joueur_courant = self.joueur_noir
        else:
            self.joueur_courant = self.joueur_blanc

    def run(self):
        print("Bienvenue dans le moteur de jeu Dames!")

        board = Board()
        board.display()

        while not self.is_game_over():
            print(f"C'est au tour du joueur {self.joueur_courant.color}.")
            move = self.joueur_courant.make_move(board)

            while not board.is_valid_move(move):
                print("Coup invalide. Réessayez.")
                move = self.joueur_courant.make_move(board)

            board.make_move(move)
            self.change_joueur()
            board.display()

        print("Partie terminée!")

    def __init__(self, joueur_blanc: BasePlayer, joueur_noir: BasePlayer, taille_plateau: int | None = 8):
        self.plateau = Board(taille=taille_plateau)
        self.joueur_blanc = joueur_blanc
        self.joueur_noir = joueur_noir
        self.joueur_courant = 1
        self.joueurs = {1: self.joueur_blanc, -1: self.joueur_noir}
        joueur_blanc.set_jeu(plateau=self.plateau, valeur_pion=1)
        joueur_noir.set_jeu(plateau=self.plateau, valeur_pion=-1)

    def change_joueur(self):
        """
        Change le joueur courant, c'est-à-dire la valeur de 'self.joueur_courant'.
        """
        self.joueur_courant *= -1

    def run(self):
        """
        Fonction principale permettant de jouer une partie en utilisant une boucle attendant la fin de la partie.
        """
        while self.plateau.etat() is None:
            print(self.plateau)
            joueur = self.joueurs[self.joueur_courant]
            coup_origine, coup_destination = joueur.joue()
            self.plateau.joue(case_origine=coup_origine, case_destination=coup_destination)
            print(f"{joueur.nom} à joué {coup_origine}-->{coup_destination}")
            input("Appuyez sur une touche...")
            print("\n")
            self.change_joueur()
        print(self.plateau)
        input("Fin de la partie, appuyez sur une touche...")


class Rules:
    """
    Description : Énonce les règles spécifiques du jeu de dames.
    Responsabilités : Valider les mouvements, détecter les conditions de victoire ou de match nul, gérer les règles spéciales (comme les sauts multiples).

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")


class Score:
    """
    Description : Suivre le score de chaque joueur pendant la partie.
    Responsabilités : Compter les pièces capturées, suivre les gains et les pertes.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")
