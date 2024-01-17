import random

from src.players.player import BasePlayer


class RandomBot(BasePlayer):
    """
    Classe utilisée pour modéliser un bot jouant des coups aléatoires.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Board) : Le plateau de jeu sur lequel joue le joueur.
            valeur_pion (int) : La valeur du pion du joueur.

        Interface :
            set_jeu(...) : Met à jour l'attribut 'self.plateau' et 'self.valeur_pion'.
            coup_valide(...) : Retourne si le coup entréé est valide.
            joue() : Retourne un coup au hasard parmi les coups possibles pouvant être joué.
    """

    def __init__(self, nom: str | None = "RandomBot"):
        super().__init__(nom)

    def joue(self):
        """
        Retourne un coup au hasard parmi les coups pouvant être joué, c'est-à-dire un couple aléatoire
        (case_origne, case_destination) provenant des coups possibles du joueur.

            Retourne :
                tuple : Retourne un tuple (case_origne, case_destination) aléatoire des coups possibles.
        """
        coups_possible = self.plateau.get_coups_possible(joueur=self.valeur_pion)
        case_origine = random.choice(list(coups_possible.keys()))
        case_destination = random.choice(coups_possible[case_origine])
        return case_origine, case_destination


class BotMinMax:
    """
    Description : Bot implémentant l'algorithme MinMax.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")


class Albator:
    """
    Description : Bot implémentant MinMax et l'élagage alpha-bêta.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")
