import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.game_engine.game import GameEngine
from src.players.player import HumanPlayer
from src.players.bots.bot import RandomBot, MinMaxBot, Albator


def choix_joueur(couleur: str):
    """
    Retourne la classe du joueur choisi après la demande de son numéro avec un input.

        Paramètre :
            couleur (str) : La couleur du joueur à afficher dans le menu lors du choix.

        Retourne :
            BasePlayer : La classe du joueur utilisé.
    """
    menu = f"""
    Choisissez le joueur {couleur} :
        1. Joueur Humain (HumanPlayer)
        2. Bot aléatoire (RandomBot)
        3. Bot MinMax (MinMaxBot)
        4. Bot AlphaBeta (Albator)
    --> """

    joueurs = {
        "1": HumanPlayer,
        "2": RandomBot,
        "3": MinMaxBot,
        "4": Albator
    }

    choix = input(menu)
    if choix in joueurs:
        return joueurs[choix]()
    raise ValueError("Choix du joueur invalide...")


if __name__ == "__main__":
    print(""" 
 ┌───────────────────────────────────────────────────────────────────────────┐
 │  _______  __   __  _______  _______  ___   _  _______  ______    _______  │
 │ |       ||  | |  ||       ||       ||   | | ||       ||    _ |  |       | │
 │ |       ||  |_|  ||    ___||       ||   |_| ||    ___||   | ||  |  _____| │
 │ |       ||       ||   |___ |       ||      _||   |___ |   |_||_ | |_____  │
 │ |      _||       ||    ___||      _||     |_ |    ___||    __  ||_____  | │
 │ |     |_ |   _   ||   |___ |     |_ |    _  ||   |___ |   |  | | _____| | │
 │ |_______||__| |__||_______||_______||___| |_||_______||___|  |_||_______| │
 └───────────────────────────────────────────────────────────────────────────┘""")

    joueur1 = choix_joueur(couleur="blanc")
    joueur2 = choix_joueur(couleur="noir")

    print("\n  ───────────────────────────────────────────────────────────────────────────\n")
    master_game = GameEngine(joueur_blanc=joueur1, joueur_noir=joueur2)
    master_game.run()
