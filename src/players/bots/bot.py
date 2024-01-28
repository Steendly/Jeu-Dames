import random

from src.players.player import BasePlayer
from src.players.bots.algorithms.minmax import MinMax


class RandomBot(BasePlayer):
    """
    Classe utilisée pour modéliser un bot jouant des coups aléatoires.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Board) : Le plateau de jeu sur lequel joue le bot.
            valeur_pion (int) : La valeur du pion du joueur.

        Interface :
            set_jeu(...) : Met à jour l'attribut 'self.plateau' et 'self.valeur_pion'.
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


class MinMaxBot(BasePlayer):
    """
    Classe utilisée pour modéliser un bot jouant utilisant l'algorithme MinMax.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Board) : Le plateau de jeu sur lequel joue le bot.
            valeur_pion (int) : La valeur du pion du joueur.
            profondeur (int) : La hauteur du graphe des coups testés (le nombre de coups successifs à tester).

        Interface :
            set_jeu(...) : Met à jour l'attribut 'self.plateau' et 'self.valeur_pion'.
            joue() : Retourne un coup au hasard parmi les coups possibles pouvant être joué.
    """

    def __init__(self, nom: str | None = "MinMaxBot", profondeur: int | None = 3):
        super().__init__(nom)
        self.profondeur = profondeur

    def joue(self):
        """
        Retourne un coup au hasard parmi les coups pouvant être joué, c'est-à-dire un couple aléatoire
        (case_origne, case_destination) provenant des coups possibles du joueur.

            Retourne :
                tuple : Retourne un tuple (case_origne, case_destination) aléatoire des coups possibles.
        """
        valeurs_coups = {}
        for coup in self.plateau.get_liste_coups_possible(joueur=self.valeur_pion):
            self.plateau.joue(case_origine=coup[0], case_destination=coup[1])
            minmax_algo = MinMax(plateau=self.plateau, profondeur=self.profondeur, joueur_actuel=self.valeur_pion)
            valeurs_coups[coup] = minmax_algo.evaluate()
            self.plateau.joue(coup[1], coup[0], True)
        if self.plateau == 1:
            return max(valeurs_coups)
        return min(valeurs_coups)


class Albator:
    """
    Description : Bot implémentant MinMax et l'élagage alpha-bêta.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")
