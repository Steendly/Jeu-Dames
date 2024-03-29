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
            nombre_pions (dict) : Un dictionnaire contenant le nombre de pions de chaque joueur.

        Interface :
            get_cases() : Retourne les cases du plateau.
            get_case(...) : Retourne la valeur de la case spécifiée si valide.
            set_case(...) : Met à jour la valeur d'une case (si valide) avec la valeur spécifiée.
            get_coups_possible(...) : Retourne les coups possibles pouvant être joués par un joueur.
            get_liste_couops_possible(...) : Retourne les coups possibles d'un joueur sous forme de liste.
            update_coups_possible(...) : Met à jour les coups possibles.
            get_nombre_pions(...) : Retourne le nombre de pions restant d'un joueur sur le plateau.
            update_nombre_pions() : Met à jour le nombre de pions restant sur le plateau de tous les joueurs.
            set_nombre_pions(...) : Met à jour le nombre de pions d'un ou plusieurs joueurs avec la valeur donné.
            add_nombre_pions(...) : Augmente de 1 ou décrémente de moins -1 le nombre de pions restant d'un joueur.
            joueur_valide(...) : Retourne si la valeur donnée d'un joueur est valide.
            case_valide(...) : Vérifie si les coordonnées d'une case sont bien valide.
            etat_case(...) : Renvoie la valeur d'une case, et si la case n'est pas valide renvoie None.
            coup_valide(...) : Retourne si un coup est valide ou non sur le plateau de jeu.
            etat() : Retourne l'état du plateau, c'est-à-dire si un joueur a gagné ou non.
            joue(...) : Vérifie et applique un coup sur le plateau.
            __str__() : Renvoie la représentation en chaîne de caractère du plateau.
    """

    def __init__(self, taille: int | None = 8, cases: dict | None = None):
        self.coups_possible = {1: {}, -1: {}}
        self.nombre_pions = {1: 0, -1: 0}
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
        self.update_nombre_pions()

    def get_cases(self):
        """
        Retourne les cases du plateau.

            Retourne :
                dict : Le dictionnaire des cases du plateau, c'est-à-dire 'self.cases'.
        """
        return self.cases

    def get_case(self, case: tuple):
        """
        Retourne la valeur de la case spécifiée si valide.

            Paramètre :
                case (tuple) : Le couple de deux entiers représentant les coordonnées de la case.

            Retourne :
                int : La valeur de la case étant -1, 0 ou 1.
        """
        assert self.case_valide(case=case), "Case invalide !"
        return self.cases[case]

    def set_case(self, case: tuple, valeur: int):
        """
        Met à jour la valeur d'une case (si valide) avec la valeur spécifiée.

            Paramètres :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.
                valeur (int) : La valeur nouvelle valeur de la case.
        """
        assert self.case_valide(case=case), "Coordonnées de la case invalide !"
        assert valeur in [-1, 0, 1], "Valeur de la case invalide !"
        self.cases[case] = valeur

    def get_coups_possible(self, joueur: int):
        """
        Retourne les coups possibles pouvant être joués par un joueur.

            Paramètre :
                joueur (int) : Le couple de deux entiers représentant les coordonnées de la case.

            Retourne :
                dict : Un dictionnaire contenant les coups possible d'un joueur avec comme clé les coordonnées de la
                       case d'origine et comme valeurs une liste des cases de destinations.
        """
        assert self.joueur_valide(joueur=joueur), "Joueur invalide !"
        return self.coups_possible[joueur]

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
        assert self.joueur_valide(joueur=joueur)
        coups_possible = self.get_coups_possible(joueur=joueur)
        liste_coups_possible = []
        for case_origine in coups_possible:
            for case_destination in coups_possible[case_origine]:
                liste_coups_possible.append((case_origine, case_destination))
        return liste_coups_possible

    def update_coups_possible(self, joueur: int):
        """
        Met à jour la liste des coups possible 'self.coups_possible' pour un joueur (-1 : noirs et 1 : blancs).

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.
        """
        assert self.joueur_valide(joueur=joueur), "Joueur invalide !"
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

    def get_nombre_pions(self, joueur: int):
        """
        Retourne le nombre de pions restant d'un joueur sur le plateau.

            Paramètre :
                joueur (int) : La valeur du joueur, 1 pour les blancs et -1 pour les noirs.

            Retourne :
                int : Le nombre de pions restant du joueur spécifié.
        """
        assert self.joueur_valide(joueur=joueur), "Joueur invalide !"
        return self.nombre_pions[joueur]

    def update_nombre_pions(self):
        """
        Met à jour le nombre de pions restant sur le plateau de tous les joueurs.
        """
        self.nombre_pions[1] = 0
        self.nombre_pions[-1] = 0
        for valeur_case in self.cases.values():
            if valeur_case:
                self.nombre_pions[valeur_case] += 1

    def set_nombre_pions(self, valeur: int, joueur: int | None = None):
        """
        Met à jour le nombre de pions d'un ou plusieurs joueurs avec la valeur donné :
        Si le paramètre 'joueur' est spécifié, seul le nombre de pions restant sur le plateau de ce joueur est
        actualisé, sinon tous les joueurs sont actualisés avec cette valeur.

            Paramètres :
                valeur (int) : Le nouveau nombre de pions restant.
                joueur (int | None) : La valeur du joueur devant être mis à jour. 1 pour les blancs, -1 pour les noirs
                                      et None pour les deux.
        """
        assert valeur >= 0, "Un nombre de pion négatif n'est pas possible !"
        if joueur is None:
            self.nombre_pions[1] = valeur
            self.nombre_pions[-1] = valeur
        else:
            assert self.joueur_valide(joueur=joueur), "Joueur invalide !"
            self.nombre_pions[joueur] = valeur

    def add_nombre_pions(self, joueur: int, valeur: int):
        """
        Augmente de 1 ou décrémente de moins -1 le nombre de pions restant d'un joueur sur le plateau en fonction du
        paramètre 'valeur'.

            Paramètres :
                joueur (int) : La valeur du joueur devant être mis à jour. 1 pour les blancs, -1 pour les noirs.
                valeur (int) : La valeur qui va être ajouté (ou enlevé) du nombre de pions restant du joueur. Peut
                               seulement être égale à 1 ou -1.
        """
        assert self.joueur_valide(joueur=joueur), "Joueur invalide !"
        assert valeur == 1 or valeur == -1, "Seulement possible d'ajouter 1 ou -1 !"
        self.nombre_pions[joueur] += valeur

    def joueur_valide(self, joueur: int):
        """
        Retourne si un joueur est valide, c'est-à-dire si son numéro correspond bien à 1 ou -1 (1 pour les blancs et
        -1 pour les noirs).

            Paramètre :
                 joueur (int) : La valeur du joueur.
        """
        return joueur == 1 or joueur == -1

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
        return self.get_case(case=case)

    def etat(self):
        """
        Retourne l'état actuel du plateau, c'est-à-dire 1/-1 si le joueur blanc/noir gagne, 0 en cas d'égalité et
        sinon None.
        """
        if len(self.get_coups_possible(joueur=1)) == 0 and len(self.get_coups_possible(joueur=-1)) == 0:
            return 0
        elif self.get_nombre_pions(joueur=1) <= 0 or len(self.get_coups_possible(joueur=1)) == 0:
            return -1
        elif self.get_nombre_pions(joueur=-1) <= 0 or len(self.get_coups_possible(joueur=-1)) == 0:
            return 1
        else:
            return None

    def coup_valide(self, case_origine: tuple, case_destination: tuple):
        """
        Retourne si un coup est valide ou non sur le plateau de jeu. Vérifie que les deux cases soient bien sûr le
        plateau (que leurs coordonnées soient valides), que la case d'origine 'case_origine' soit bien une case d'un
        joueur et que la case de destination 'case_destination' soit vide.

            Paramètres :
                case_origine (tuple) : Tuple de deux entiers contenant les coordonnées de la case d'origine.
                case_destination (tuple) : Tuple de deux entiers contenant les coordonnées de la case de destination.

            Retourne :
                bool : True si le coup est valide et False dans le cas contraire.
        """
        if (not self.case_valide(case=case_origine)) or (not self.case_valide(case=case_destination)):
            return False
        valeur_case = self.get_case(case=case_origine)
        if valeur_case == 0:
            return False
        return ((case_origine in self.get_coups_possible(joueur=valeur_case))
                and (case_destination in self.get_coups_possible(joueur=valeur_case)[case_origine]))

    def joue(self, case_origine: tuple, case_destination: tuple, coup_inverse: bool | None = False):
        """
        Vérifie et applique le coup s'il est valide sur le plateau de jeu. Un coup est décomposé en deux cases :
        la case d'origine et la case de destination. Trois coups différents peuvent être joués :
            - un déplacement : il s'agit d'un déplacement de pion d'une case. La valeur de la case d'origine est
                               simplement transféré à la case de destination
            - une prise de pièce : un pion prend un pion adverse, c'est-à-dire qu'il lui passe au-dessus. La valeur de
                                   la case d'origine est transféré à la case de destination et le pion entre le chemin
                                   de ces deux cases est supprimé
            - un coup inverse : il s'agit d'annuler une prise de pièce, ou un déplacement. Se comporte de la même
                                manière que les deux autres coups possibles, à la différence qu'il n'est pas vérifié
                                si la case d'origine et de destination sont présente dans les coups possibles.

            Paramètres :
                case_origine (tuple) : Tuple de deux entiers contenant les coordonnées de la case d'origine.
                case_destination (tuple) : Tuple de deux entiers contenant les coordonnées de la case de destination.
                coup_inverse (bool | None) : Booléen qui indique s'il s'agit d'un coup inverse ou non.
        """
        if coup_inverse and not (self.case_valide(case=case_origine) and self.case_valide(case=case_destination)):
            raise ValueError("Coup inverse invalide : case d'origine/destination pas dans le plateau !")
        if not coup_inverse and not self.coup_valide(case_origine=case_origine, case_destination=case_destination):
            raise ValueError("Coup invalide : case d'origine/destination non présente dans les coups possibles !")

        valeur_case_origine = self.get_case(case=case_origine)
        self.set_case(case=case_destination, valeur=valeur_case_origine)
        self.set_case(case=case_origine, valeur=0)
        if (abs(case_destination[0]-case_origine[0]) == 2) and (abs(case_destination[1]-case_origine[1]) == 2):
            case_milieu = ((case_origine[0]+case_destination[0])//2, (case_origine[1]+case_destination[1])//2)
            if coup_inverse:
                self.add_nombre_pions(joueur=valeur_case_origine*-1, valeur=1)
                self.set_case(case=case_milieu, valeur=valeur_case_origine*-1)
            else:
                self.add_nombre_pions(joueur=self.get_case(case=case_milieu), valeur=-1)
                self.set_case(case=case_milieu, valeur=0)
        self.update_coups_possible(joueur=1)
        self.update_coups_possible(joueur=-1)

    def __str__(self):
        """
        Retourne la representation du plateau sous forme de chaine de caractère.

            Retourne :
                str : Le plateau sous forme d'une chaine de caractère.
        """
        res = "    "
        for k in range(self.taille):
            res += f" {k} "
        res += "\n"
        res += "  ┌" + "─" * ((self.taille * 3) + 2) + "┐\n"
        for i in range(self.taille):
            res += str(i) + " │ "
            for j in range(self.taille):
                if (j + (i % 2)) % 2:
                    res += "\x1b[1;37;40m"
                else:
                    res += "\x1b[1;37;47m"
                if self.cases[(i, j)] == 1:
                    res += " B "
                elif self.cases[(i, j)] == -1:
                    res += " N "
                else:
                    res += "   "
            res += "\x1b[m │\n"
        res += "  └" + "─" * ((self.taille * 3) + 2) + "┘\n"
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
