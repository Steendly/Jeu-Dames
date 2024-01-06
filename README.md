# Jeu de Dames


Implémentation du jeu de Dames en Python. 
Ce projet se divise en deux grandes parties.
La première consiste en la création d'un moteur de jeu chargé de gérer le plateau, les mouvements et les règles du jeu.
La seconde partie s'articule autour de l'implémentation de bots capables de jouer au jeu, en mettant en œuvre des 
algorithmes tels que MinMax et l'élagage alpha-bêta.

---

## Structure

```
    └── src
        ├── game_engine
        │   ├── board.py
        │   ├── game.py
        │   └── gui.py
        ├── main.py
        ├── players
        │   ├── bots
        │   │   ├── algorithms
        │   │   │   ├── alpha_beta.py
        │   │   │   └── minmax.py
        │   │   └── bot.py
        │   └── player.py
        └── utils.py
```

* **game_engine/** : Module de gestion du moteur de jeu.
  * board.py : Implémentation du plateau.
  * game.py : Cœur du moteur de jeu.
  * gui.py : Interface utilisateur.
* **players/** : Module de gestion des joueurs (humains et bots).
* player.py : Implémentation de(s) classe(s) pour les joueurs humains.
  * **bots/** : Sous module de gestion des bots.
  * bot.py : Fichier regroupant les classes principales de tous les futurs bots.
    * **algorithms/** : Sous module de gestion des algorithmes pour les bots.
      * alpha_beta.py : Implémentation de l’élagage alpha-bêta.
      * minmax.py : Implémentation de l’algorithme MinMax.

---