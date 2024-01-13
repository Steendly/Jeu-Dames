import re

from src.game_engine.board import Board


class BasePlayer:
    """
    Classe utilisée pour modéliser un joueur.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Board) : Le plateau de jeu sur lequel joue le joueur.
            valeur_pion (int) : La valeur du pion du joueur.

        Interface :
            set_jeu(...) : Met à jour l'attribut 'self.plateau' et 'self.valeur_pion'.
    """

    def __init__(self, nom: str):
        self.nom = nom
        self.plateau = None
        self.valeur_pion = None

    def set_jeu(self, plateau: Board, valeur_pion: int):
        """
        Met à jour le plateau 'self.plateau' et la valeur du pion 'self.valeur_pion'.

            Paramètres :
                plateau (Board) : Le plateau sur lequel joue le joueur.
                valeur_pion (int) : La valeur du pion du joueur.
        """
        assert valeur_pion == 1 or valeur_pion == -1, "Valeur du pion invalide !"
        self.plateau = plateau
        self.valeur_pion = valeur_pion

    def joue(self):
        raise NotImplemented("Un joueur abstrait ne peut pas jouer")


class HumanPlayer(BasePlayer):
    """
    Classe utilisée pour modéliser un joueur humain héritant de BasePlayer.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Board) : Le plateau de jeu sur lequel joue le joueur.
            valeur_pion (int) : La valeur du pion du joueur.

        Interface :
            set_jeu(...) : Met à jour l'attribut 'self.plateau' et 'self.valeur_pion'.
            coup_valide(...) : Retourne si le coup entréé est valide.
            joue() : Demande au joueur de saisir un coup à jouer, et retourne le coup entréé si valide.
    """
    def __init__(self, nom: str | None = "Toto"):
        super().__init__(nom)

    def coup_valide(self, case_origine_input: str, case_destination_input: str):
        """
        Retourne si le coup entréé de la forme 'X,Y' avec X un entier, une virgule et Y un entier soit valide.

            Paramètre :
                entree (str) : Le coup joué.

            Retourne :
                bool : True si le coup est valide, False sinon.
        """
        motif = re.compile(r"[0-9],[0-9]$")
        if (motif.match(case_origine_input) is None) or (motif.match(case_destination_input) is None):
            return False
        case_origine = (int(case_origine_input[0]), int(case_origine_input[2]))
        case_destination = (int(case_destination_input[0]), int(case_destination_input[2]))
        return self.plateau.coup_valide(case_origine=case_origine, case_destination=case_destination)

    def joue(self):
        """
        Demande au joueur de saisir un coup à jouer, c'est-à-dire en premier les cordonnées de la case où est le pion
        qu'il veut déplacer 'case_origine' et en deuxième les coordonnées de la case où il veut déplacer ce pion
        'case_destination'. Redemande de saisir le coup tant qu'il n'est valide.

            Retourne :
                tuple : Deux tuples représentant dans l'ordre qui suit les cordonnées de la case d'origine et de la
                        case de destination.
        """
        case_origine = input("Entrez votre coup :\n   Case d'origine -> ")
        case_destination = input("   Case de destination -> ")
        while not self.coup_valide(case_origine_input=case_origine, case_destination_input=case_destination):
            print("\nCoup invalide !")
            case_origine = input("Entrez votre coup :\n   Case d'origine -> ")
            case_destination = input("   Case de destination -> ")
        return (int(case_origine[0]), int(case_origine[2])), (int(case_destination[0]), int(case_destination[2]))
