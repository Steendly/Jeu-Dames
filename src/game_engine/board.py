from math import sqrt


class Board:
    """
    Classe utilisée pour modéliser un plateau de jeu.
    Ses dimensions doivent être comprises entre 4 et 10 inclus et être pairs.
    Chaque case du plateau est représentée par son couple de coordonnées avec sa valeur :
        * 0 pour les cases vides
        * 1 pour les pions blancs
        * -1 pour les pions noirs
    de la forme suivante dans un dictionnaire : {(x, y): value, ...}.

        Attributs :
            cases (dict) : Un dictionnaire contenant toutes les cases du jeu avec leurs valeurs.
            taille (int) : Taille du plateau, c'est-à-dire la taille de sa largeur et de sa hauteur.
            coups_possible (dict) : Un dictionnaire contenant les coups possible pouvant être joués.

        Interface :
            case_valide(...) : Vérifie si les coordonnées d'une case sont bien valide.
            etat_case(...) : Renvoie la valeur d'une case, et si la case n'est pas valide renvoie None.
            joue(...) : Vérifie et applique un coup sur le plateau.
            update_coups_possible(...) : Met à jour les coups possibles.
            coup_valide(...) : Retourne si un coup est valide ou non sur le plateau de jeu.
            __str__() : Renvoie la représentation en chaîne de caractère du plateau.
    """

    def __init__(self, taille: int | None = 8, cases: dict | None = None):
        self.coups_possible = {1: {}, -1: {}}
        if cases is None:
            assert 4 <= taille <= 10 and taille % 2 == 0
            self.taille = taille
            self.cases = {}
            for i in range(self.taille):
                for j in range(self.taille):
                    if (0 <= i <= (((self.taille - 2) // 2) - 1)) and ((j + (i % 2)) % 2):
                        self.cases[(i, j)] = -1
                    elif (i >= ((self.taille // 2) + 1)) and ((j + (i % 2)) % 2):
                        self.cases[(i, j)] = 1
                    else:
                        self.cases[(i, j)] = 0
        else:
            taille = sqrt(len(self.cases))  # ajouter plus de vérification
            assert taille % 2 == 0 and 4 <= taille <= 10
            self.taille = int(taille)
            self.cases = cases
        self.update_coups_possible(joueur=1)
        self.update_coups_possible(joueur=-1)

    def case_valide(self, case: tuple):
        """
        Vérifie si les coordonnées de la case sont valides, c'est-à-dire qu'elles font bien partie du plateau.

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.

            Retourne :
                bool : True si les coordonnées de la case sont valides, sinon False.
        """
        return all(0 <= coord <= (self.taille - 1) for coord in case)

    def etat_case(self, case: tuple):
        """
        Retourne la valeur d'une case (-1, 0 ou 1), et si les coordonnées de la case ne font pas parties du plateau None.

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.

            Retourne :
                int : La valeur de la case si cette dernière est valide.
                NoneType : None si la case n'est pas valide.
        """
        if not self.case_valide(case=case):
            return None
        return self.cases[case]

    def update_coups_possible(self, joueur: int):
        """
        Met à jour la liste des coups possible 'self.coups_possible' pour un joueur (-1 : noirs et 1 : blancs).

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.
        """
        assert joueur == 1 or joueur == -1, "Joueur invalide !"
        self.coups_possible[joueur] = {}
        for case, valeur_case in self.cases.items():
            if valeur_case == joueur:
                self.coups_possible[joueur][case] = []
                cg = (case[0] - joueur, case[1] - 1)  # case gauche
                cd = (case[0] - joueur, case[1] + 1)  # case droite
                cg_2 = (cg[0] - joueur, cg[1] - 1)  # case gauche de la case gauche
                cd_2 = (cd[0] - joueur, cd[1] + 1)  # case droite de la case droite
                etat_cg = self.etat_case(case=cg)
                etat_cd = self.etat_case(case=cd)
                if etat_cg == 0:
                    self.coups_possible[joueur][case].append(cg)
                elif etat_cg == -joueur and self.etat_case(case=cg_2) == 0:
                    self.coups_possible[joueur][case].append(cg_2)
                if etat_cd == 0:
                    self.coups_possible[joueur][case].append(cd)
                elif etat_cd == -joueur and self.etat_case(case=cd_2) == 0:
                    self.coups_possible[joueur][case].append(cd_2)
                if len(self.coups_possible[joueur][case]) == 0:
                    self.coups_possible[joueur].pop(case)

    def coup_valide(self, case_origine: tuple, case_destination: tuple):
        """
        Retourne si un coup est valide ou non sur le plateau de jeu. Vérifie que les deux cases soient bien sûr le
        plateau (que leurs coordonnées soient valides), que la case d'origine 'case_origine' soit bien une case d'un
        joueur et que la case de destination 'case_destination' soit vide.

            Paramètre :
                case_origine (tuple) : Tuple de deux entiers contenant les coordonnées de la case d'origine.
                case_destination (tuple) : Tuple de deux entiers contenant les coordonnées de la case de destination.

            Retourne :
                bool : True si le coup est valide et False dans le cas contraire.
        """
        if (not self.case_valide(case=case_origine)) or (not self.case_valide(case=case_destination)):
            return False
        valeur_case = self.cases[case_origine]
        if valeur_case == 0:
            return False
        return ((case_origine in self.coups_possible[valeur_case])
                and (case_destination in self.coups_possible[valeur_case][case_origine]))

    def joue(self, case_origine: tuple, case_destination: tuple):
        """
        Vérifie et applique le coup s'il est valide sur le plateau de jeu. Un coup est décomposé en deux cases :
        la case d'origine et la case de destination. Deux coups différents peuvent être joués :
            - un déplacement : il s'agit d'un déplacement de pion d'une case. La valeur de la case d'origine est
                               simplement transféré à la case de destination
            - une prise de pièce : un pion prend un pion adverse, c'est-à-dire qu'il lui passe au-dessus. La valeur de
                                   la case d'origine est transféré à la case de destination et le pion entre le chemin
                                   de ces deux cases est supprimé/

            Paramètre :
                case_origine (tuple) : Tuple de deux entiers contenant les coordonnées de la case d'origine.
                case_destination (tuple) : Tuple de deux entiers contenant les coordonnées de la case de destination.
        """
        if self.coup_valide(case_origine=case_origine, case_destination=case_destination):
            valeur_pion = self.cases[case_origine]
            self.cases[case_origine] = 0
            self.cases[case_destination] = valeur_pion
            if (abs(case_origine[0]-case_destination[0]) == 2) and (abs(case_origine[1]-case_destination[1]) == 2):
                self.cases[((case_origine[0]+case_destination[0])//2, (case_origine[1]+case_destination[1])//2)] = 0
            self.update_coups_possible(joueur=1)
            self.update_coups_possible(joueur=-1)
        else:
            raise ValueError("Coup invalide : case d'origine/destination non présente dans les coups possibles !")

    def __str__(self):
        """
        Retourne la representation du plateau sous forme de chaine de caractère.

            Retourne :
                str : Le plateau sous forme d'une chaine de caractère.
        """
        res = "   "
        for k in range(self.taille):
            res += f" {k}"
        res += "\n"
        res += "  ┌" + "─" * ((self.taille * 2) + 1) + "┐\n"
        for i in range(self.taille):
            res += str(i) + " │ "
            for j in range(self.taille):
                if self.cases[(i, j)] == 1:
                    res += "B "
                elif self.cases[(i, j)] == -1:
                    res += "N "
                else:
                    res += ". "
            res += "│\n"
        res += "  └" + "─" * ((self.taille * 2) + 1) + "┘\n"
        return res


class Square:
    """
    Description : Chaque case du plateau de jeu où une pièce peut être placée.
    Responsabilités : Contenir ou ne pas contenir une pièce, gérer les positions sur le plateau.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")


class Piece:
    """
    Description : Les pions ou rois que les joueurs déplacent sur le plateau.
    Responsabilités : Suivre à quel joueur la pièce appartient, gérer les mouvements spécifiques aux pions ou rois.

    /!\ Non implémentée !
    """

    def __init__(self):
        raise NotImplemented("Classe no implémentée !")
