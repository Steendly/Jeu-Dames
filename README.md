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


## Utilisation

Pour lancer le projet, exécuter la commande ci-dessous à sa racine :
```bash
python3 -m src.main
```

Voici un petit aperçu :
```
 ┌───────────────────────────────────────────────────────────────────────────┐
 │  _______  __   __  _______  _______  ___   _  _______  ______    _______  │
 │ |       ||  | |  ||       ||       ||   | | ||       ||    _ |  |       | │
 │ |       ||  |_|  ||    ___||       ||   |_| ||    ___||   | ||  |  _____| │
 │ |       ||       ||   |___ |       ||      _||   |___ |   |_||_ | |_____  │
 │ |      _||       ||    ___||      _||     |_ |    ___||    __  ||_____  | │
 │ |     |_ |   _   ||   |___ |     |_ |    _  ||   |___ |   |  | | _____| | │
 │ |_______||__| |__||_______||_______||___| |_||_______||___|  |_||_______| │
 └───────────────────────────────────────────────────────────────────────────┘

    Choisissez le joueur blanc:
        1. Joueur Humain (HumanPlayer)
        2. Bot aléatoire (RandomBot)
        3. Bot MinMax (MinMaxBot)
    --> 1

    Choisissez le joueur noir:
        1. Joueur Humain (HumanPlayer)
        2. Bot aléatoire (RandomBot)
        3. Bot MinMax (MinMaxBot)
    --> 3

  ───────────────────────────────────────────────────────────────────────────

     0  1  2  3  4  5  6  7 
  ┌──────────────────────────┐
0 │     N     N     N     N  │
1 │  N     N     N     N     │
2 │     N     N     N     N  │
3 │                          │
4 │                          │
5 │  B     B     B     B     │
6 │     B     B     B     B  │
7 │  B     B     B     B     │
  └──────────────────────────┘
Entrez votre coup...
```
Le tout avec le plateau en couleur si vous l'exécuté dans un terminal supportant les séquences d'échappement ANSI.