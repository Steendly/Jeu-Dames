import math

from src.game_engine.board import Board


class MinMax:
    """
    Description : Classe implémentant l'algorithme MinMax.

        blanc (1) : maximizing score
        noir (-1) : minimise score

        Attributs :
            plateau (Board) : Le plateau de jeu à évaluer.
            joueur_actuel (int) : Le joueur qui doit actuellement jouer sur ce plateau.
            profondeur (int) : La hauteur du graphe des coups testés (le nombre de coups successifs à tester).

        Interface :
            get_liste_coups_possible(...) : Retourne une liste de tuple des coups possibles d'un joueur.
            evaluate_node() : Retourne la valeur heuristique du plateau actuel (fonction d'évaluation).
            _evaluate(...) : Retourne récursivement la valeur d'un plateau en suivant l'algorithme MinMax.
            evaluate(...) : Initialise l'appel de '_evaluate' et retourne sa valeur.
    """
    def __init__(self, plateau: Board, joueur_actuel: int, profondeur: int):
        self.plateau = plateau
        self.joueur_actuel = joueur_actuel
        self.profondeur = profondeur

    def get_liste_coups_possible(self, joueur: int):
        """
        Retourne une liste de tuple des coups possibles d'un joueur sur le plateau actuel de la forme :
        [(case_origine, case_destination), ...] avec 'case_origine' les coordonnées (x, y) de la case d'origine du coup
        et 'case_destination' les coordonnées (x, y) de la case de destination du coup.

            Paramètre :
                joueur (int) : La valeur du joueur, 1 pour les blancs et -1 pour les noirs.

            Retourne :
                list : La liste des coups possible du joueur en question.
        """
        assert self.plateau.joueur_valide(joueur=joueur)
        coups_possible = self.plateau.get_coups_possible(joueur=joueur)
        liste_coups_possible = []
        for case_origine in coups_possible:
            for case_destination in coups_possible[case_origine]:
                liste_coups_possible.append((case_origine, case_destination))
        return liste_coups_possible

    def evaluate_node(self):
        """
        Fonction d'évaluation retournant la valeur heuristique du plateau actuel. Calcule simplement le nombre de pions
        du joueur blanc moins le nombre de pions du joueur noir.

            Retourne :
                int : La valeur heuristique du plateau actuel.
        """
        return self.plateau.get_nombre_pions(joueur=1) - self.plateau.get_nombre_pions(joueur=-1)

    def _evaluate(self, profondeur: int, maximizing_joueur: bool):
        """
        Fonction implémentant l'algorithme MinMax récursivement avec du backtracking. Son exécution est associée à un
        arbre avec comme nœuds un état du plateau en fonction des coups possible de chaque joueur. La valeur de ses
        feuilles est renvoyée par la fonction d'évaluation 'evaluate_node()'.

            Paramètre :
                profondeur (int) : La hauteur du graphe d'exécution de la fonction, c'est-à-dire le nombre de coups
                                   possibles testés successivement.
                maximizing_joueur (bool) : Indique si le joueur qui doit jouer actuellement est le maximizing player,
                                           autrement dit le joueur qui doit maximiser son score (le joueur blanc).

            Retourne :
                int : La valeur du plateau calculé avec l'algorithme MinMax.
        """
        if profondeur == 0:
            return self.evaluate_node()
        if maximizing_joueur:
            max_valeur = -math.inf
            for coup in self.get_liste_coups_possible(joueur=1):
                self.plateau.joue(coup[0], coup[1])
                ev = self._evaluate(profondeur=profondeur-1, maximizing_joueur=False)
                self.plateau.joue(coup[1], coup[0], True)
                max_valeur = max(max_valeur, ev)
            return max_valeur
        else:
            min_valeur = math.inf
            for coup in self.get_liste_coups_possible(joueur=-1):
                self.plateau.joue(coup[0], coup[1])
                ev = self._evaluate(profondeur=profondeur-1, maximizing_joueur=True)
                self.plateau.joue(coup[1], coup[0], True)
                min_valeur = min(min_valeur, ev)
            return min_valeur

    def evaluate(self):
        """
        Initialise l'appel de la fonction '_evaluate(...)' avec les paramètres correspondants et retourne sa valeur.

            Retourne :
                int : La valeur du plateau retourné par '_evaluate(...)'.
        """
        return self._evaluate(profondeur=self.profondeur, maximizing_joueur=(lambda x: x*1 == 1)(self.joueur_actuel))
