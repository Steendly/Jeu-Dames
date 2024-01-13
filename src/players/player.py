from src.game_engine.board import Board


class BasePlayer:
    """
    Classe utilisée pour modéliser un joueur.

        Attributs :
            nom (str) : Le nom du joueur.
            plateau (Grille) : Le plateau de jeu sur lequel joue le joueur.
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
