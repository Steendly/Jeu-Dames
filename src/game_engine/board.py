from math import sqrt


class Board:
    """
    Classe utilisée pour modéliser un plateau.

        Attributs :
            cases (dict) : Un dictionnaire contenant toutes les cases du jeu avec leurs valeurs.
            taille (int) : Taille du plateau, c'est-à-dire la taille de sa largeur et de sa hauteur.
            cases_vides (list) : La liste des cases vides du plateau.

        Interface :
            update_cases_vides() : Met à jour la liste des cases vides 'self.vides'.
            est_vide(...) : Retourne si oui ou non une case est vide.
            case_valide(...) : Vérifie si les coordonnées d'une case sont bien valide.
            get_vides(...) : Retourne la liste des cases vides.
            joue(...) : Vérifie et applique un coup sur le plateau.
            __str__() : Renvoie la représentation en chaîne de caractère du plateau.
    """
    def __init__(self, taille: int | None = 8, cases: dict | None = None):
        self.cases_vides = []
        if not cases:
            assert 4 <= taille <= 10 and taille % 2 == 0
            self.taille = taille
            end_i_noir = ((self.taille - 2) // 2) - 1
            end_i_blanc = (self.taille // 2) + 1
            self.cases = {}
            for i in range(self.taille):
                for j in range(self.taille):
                    if (0 <= i <= end_i_noir) and ((j + (i % 2)) % 2):
                        self.cases[(i, j)] = -1
                    elif (i >= end_i_blanc) and ((j + (i % 2)) % 2):
                        self.cases[(i, j)] = 1
                    else:
                        self.cases[(i, j)] = 0
                        self.cases_vides.append((i, j))
        else:
            taille = sqrt(len(self.cases))
            assert taille % 2 == 0 and 4 <= taille <= 10
            self.taille = int(taille)
            self.cases = cases
            self.update_cases_vides()

    def update_cases_vides(self):
        """
        Met à jour la liste des cases vides contenue dans 'self.cases_vides'.
        """
        self.cases_vides = []
        for i in range(self.taille):
            for j in range(self.taille):
                if self.cases[(i, j)] == 0:
                    self.cases_vides.append((i, j))

    def est_vide(self, case: tuple):
        """
        Vérifie si une case est vide ou non.

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.

            Retourne :
                bool : True si la case est vide, sinon False.
        """
        return self.cases[case] == 0

    def get_vides(self, update: bool | None = False):
        """
        Met à jour les cases vides si 'update' est à True et retourne la liste des cases vides,
        c'est-à-dire 'self.cases_vides'.

            Paramètre :
                update (bool) : Si True, met à jour les cases vides avec la méthode 'self.update_cases_vides'.

            Retourne :
                list: Retourne self.cases_vides.
        """
        if update:
            self.update_cases_vides()
            return self.cases_vides
        return self.cases_vides

    def case_valide(self, case: tuple):
        """
        Vérifie si les coordonnées de la case sont valides, c'est-à-dire qu'elles font bien partie du plateau.

            Paramètre :
                case (tuple) : Tuple de deux entiers contenant les coordonnées de la case.

            Retourne :
                bool : True si les coordonnées de la case sont valides, sinon False.
        """
        return all(0 <= coord <= (self.taille - 1) for coord in case)

    def joue(self, case: tuple, valeur_pion: int):
        """
        Vérifie et applique le coup s'il est valide sur le plateau, c'est-à-dire vérifie que la case 'case' soit comprise
        dans le plateau et qu'elle soit vide, et ensuite applique la valeur du pion 'valeur_pion' sur cette case.

            Paramètre :
                case (tuple) : La case ou appliquer le coup.
                valeur_pion (int) : La valeur du pion du coup.
        """
        if not (self.case_valide(case=case) and (self.est_vide(case=case))):
            raise ValueError("Case invalide")
        self.cases[case] = valeur_pion
        self.update_cases_vides()

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
        res += "  ┌" + "─"*((self.taille*2)+1) + "┐\n"
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
