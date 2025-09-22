import graph
import random
from typing import *
from collections import deque
from Labyrinthe import *

class TP1:
    def __init__(self: Self) -> None:
        print("Exploring python")

class TP2:
    def a_la_chaine(self: Self, n: int) -> str:
        return 'A' * n
    
    def a_la_chaine2(self: Self, esp: int, n: int) -> str:
        return ' ' * esp + 'A' * n
    
    def colonne(self: Self, n: int) -> None:
        for _ in range(10):
            print('A' * n)

    def diagonal1(self: Self, n: int) -> None:
        for i in range(n):
            print('A' * i)
    
    def diagonal2(self: Self, n: int) -> None:
        for i in range(n):
            print(' ' * (n - i) + 'A' * i)

    def sapin_c(self: Self, n: int) -> None:
        for i in range(n):
            print(' ' * (n - i - 1) + 'A' * (2 * i - 1))
        print(' ' * (n - 3) + 'A' * (n // 3))

    def ligne_horiz(self: Self, y: int, larg: int) -> None:
        for x in range(larg):
            graph.plot(y, x)
            graph.refresh()

    def segment_horiz(self: Self, y: int, x1: int, x2: int) -> None:
        for x in range(x1, x2 + 1):
            graph.plot(y, x)
            graph.refresh()

    def rectangle(self: Self, y1: int, y2: int, x1: int, x2: int, color: str="black", refresh: bool=False) -> None:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                graph.plot(y, x, color)
                if refresh:
                    graph.refresh()

    def rayure_vertic(self: Self, haut: int, larg: int, larg_bande: int) -> None:
        for x in range(larg_bande, larg, larg_bande * 2):
            self.rectangle(0, haut - 1, x, x + larg_bande - 1)

    def damier(self: Self, haut: int, larg: int, cote: int) -> None:
        for y in range(0, haut, cote):
            for x in range(0, larg, cote):
                if (y // cote + x // cote) % 2 == 1:
                    self.rectangle(y, y + cote - 1, x, x + cote - 1)
                    graph.refresh()

    def sapin_g(self: Self, haut: int, larg: int) -> None:
        milieu: int = larg // 2
        hauteur: int = int(haut * 0.9)

        for y in range(hauteur):
            x1: int = milieu - y
            x2: int = milieu + y

            if x1 > 0 and x2 < larg:
                for x in range(x1, x2 + 1):
                    graph.plot(y, x)
                    graph.refresh()

        self.rectangle(hauteur - 28, haut - 1, milieu - 20, milieu + 20)

class TP3:
    def sapin_noel(self: Self, n: int) -> None:
        for i in range(n):
            print(' ' * (n - i), end="")
            for _ in range(2 * i - 1):
                if random.random() <= 0.2:
                    print('O', end="")
                else:
                    print('*', end="")
            print()
        print(' ' * (n - 3) + '*' * (n // 3))

    def noir(self: Self, haut: int, larg: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                graph.plot(y, x)
            graph.refresh()
        
        graph.wait()
        graph.close()

    def bande_noir_gauche(self: Self, haut: int, larg: int, larg_bande: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                if x < larg_bande:
                    graph.plot(y, x)
            graph.refresh()
        
        graph.wait()
        graph.close()

    def rectangle_noir(self: Self, haut: int, larg: int, y1: int, y2: int, x1: int, x2: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                if (x >= x1 and x <= x2) and (y >= y1 and y <= y2):
                    graph.plot(y, x)
            graph.refresh()

        graph.wait()
        graph.close()

    def rectangle_blanc(self: Self, haut: int, larg: int, y1: int, y2: int, x1: int, x2: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                if (x < x1 or x > x2) or (y < y1 or y > y2):
                    graph.plot(y, x)
            graph.refresh()

        graph.wait()
        graph.close()

    # nv = x // larg_bande
    # nv % 2 == 1

    def rayures_verticales(self: Self, haut: int, larg: int, larg_bande: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                nv: int = x // larg_bande
                if nv % 2 == 1:
                    graph.plot(y, x)
            graph.refresh()
        
        graph.wait()
        graph.close()

    # nh = y // cote
    # nv = x // cote
    # nh + nv % 2 == 1

    def damier(self: Self, haut: int, larg: int, cote: int) -> None:
        graph.open_win(haut, larg)

        for y in range(haut):
            for x in range(larg):
                nv: int = x // cote
                nh: int = y // cote

                if (nv + nh) % 2 == 1:
                    graph.plot(y, x)
            graph.refresh()
        
        graph.wait()
        graph.close()

    def damier_multicolor(self: Self, haut: int, larg: int, cote: int) -> None:
        graph.open_win(haut, larg)


        nb_case_y: int = (haut + cote - 1) // cote
        nb_case_x: int = (larg + cote - 1) // cote
        
        for nh in range(nb_case_y):
            for nv in range(nb_case_x):
                if (nh + nv) % 2 == 1:
                    color: str = random.choice(graph.Screen.DEFAULT_COLOR)
                    for y in range(nh * cote, (nh + 1) * cote):
                        for x in range(nv * cote, (nv + 1) * cote):
                            graph.plot(y, x, color)        
            graph.refresh()

        graph.wait()
        graph.close()

class TP4:
    def __init__(self: Self) -> None:
        self.tp2: TP2 = TP2()
        self.MUR: int = 0
        self.CHEMIN: int = 1
        self.ENTREE: int = 2
        self.SORTIE: int = 3

    def multiple_2(self: Self, lst: List[int]) -> None:
        for i in range(len(lst)):
            lst[i] *= 2
    
    def divisible(self: Self) -> List[int]:
        return [i for i in range(1, 101) if i % 2 == 0 or i % 3 == 0]

    def multiple_2_copy(self: Self, lst: List[int]) -> List[int]:
        return [i * 2 for i in lst]

    def pixels_voisins(self: Self, y: int, x: int) -> List[Tuple[int, int]]:
        return [
            (y, x + 1),  # right
            (y, x - 1),  # left
            (y + 1, x),  # down
            (y - 1, x),  # up
        ]

    def largeur_image(self: Self, lst: List[int], largeur_bande: int) -> int:
        return len(lst) * largeur_bande

    def num_bande(self: Self, y: int | None, x: int, largeur_bande: int) -> int:
        return x // largeur_bande # pas besoin de l'argument y
    
    def dessine_bandes1(self: Self, lst: List[int], hauteur: int, largeur_bandes: int) -> None:
        # Plus de test donc moins rapide
        largeur: int = self.largeur_image(lst, largeur_bandes)
        graph.open_win(hauteur, largeur)

        for y in range(hauteur):
            for x in range(largeur):
                bandes: int = self.num_bande(None, x, largeur_bandes)
                if lst[bandes] == 0:
                    graph.plot(y, x)
                    graph.refresh()

        graph.wait()
        graph.close()

    def dessine_bandes2(self: Self, lst: List[int], hauteur: int, largeur_bandes: int) -> None:
        # moins de test donc plus rapide
        largeur: int = self.largeur_image(lst, largeur_bandes)
        graph.open_win(hauteur, largeur)

        for i in range(len(lst)):
            x1: int = i * largeur_bandes
            x2: int = (i + 1) * largeur_bandes - 1    
            
            if lst[i] == 0: 
                self.tp2.rectangle(0, hauteur - 1, x1, x2)
                graph.refresh()
        
        graph.wait()
        graph.close()

    def nb_linge(self: Self, lst: List[List[int]]) -> int:
        return len(lst)

    def nb_colonne(self: Self, lst: List[List[int]]) -> int:
        return len(lst[0])

    def taille_image(self: Self, lstlst: List[List[int]], taille: int) -> Tuple[int,int]:
        return (self.nb_linge(lstlst) * taille, self.nb_colonne(lstlst) * taille)

    def dessine_grille(self: Self, lstlst: List[List[int]], taille: int) -> None:
        taille_img: Tuple[int, int]  = self.taille_image(lstlst, taille)
        graph.open_win(taille_img[0], taille_img[1])

        for i in range(len(lstlst)):
            for j in range(len(lstlst[i])):
                x1: int = j * taille
                x2: int = (j + 1) * taille - 1
                y1: int = i * taille
                y2: int = (i + 1) * taille - 1

                if lstlst[i][j] == 0:
                    self.tp2.rectangle(y1, y2, x1, x2)
                    graph.refresh()
        graph.wait()
        graph.close()

    def entree(self: Self, laby: List[List[int]]) -> Tuple[int, int] | None:
        for i in range(len(laby)):
            for j in range(len(laby[i])):
                if laby[i][j] == self.ENTREE:
                    return (i, j)
        return None

    def sorite(self: Self, laby: List[List[int]]) -> Tuple[int, int] | None:
        for i in range(len(laby)):
            for j in range(len(laby[i])):
                if laby[i][j] == self.SORTIE:
                    return (i, j)
        return None

    def dessine_laby(self: Self, laby: List[List[int]], taille: int) -> None:
        img_taille: Tuple[int, int] = self.taille_image(laby, taille)
        graph.open_win(img_taille[0], img_taille[1])

        for i in range(len(laby)):
            for j in range(len(laby[i])):
                x1: int = j * taille
                x2: int = (j + 1) * taille - 1
                y1: int = i * taille
                y2: int = (i + 1) * taille - 1
                if laby[i][j] == self.MUR:
                    self.tp2.rectangle(y1, y2, x1, x2, "black")
                if laby[i][j] == self.CHEMIN:
                    self.tp2.rectangle(y1, y2, x1, x2, "white")
                if  laby[i][j] == self.ENTREE:
                    self.tp2.rectangle(y1, y2, x1, x2, "blue")
                if laby[i][j] == self.SORTIE:
                    self.tp2.rectangle(y1, y2, x1, x2, "red")

        graph.wait()
        graph.close()

class TP5:
    def __init__(self: Self) -> None:
        self.MUR: int = 0
        self.CHEMIN: int = 1
        self.ENTREE: int = 2
        self.SORTIE: int = 3
        self.tp2: TP2 = TP2()

    def indice(self: Self, lst: List, n: int) -> int | None:
        return next((i for i, v in enumerate(lst) if v == n), None)        

    def coord(self: Self, laby: List[List[int]], n: int) -> Tuple[int, int] | None:
        for i, v in enumerate(laby):
            j = self.indice(v, n)
            if j is not None:
                return (i, j)
        return None

    def entree(self: Self, laby: List[List[int]]) -> Tuple[int, int] | None:
        coord_entree = self.coord(laby, self.ENTREE)
        return None if coord_entree is None else coord_entree

    def sortie(self: Self, laby: List[List[int]]) -> Tuple[int, int] | None:
        coord_sortie = self.coord(laby, self.SORTIE)        
        return None if coord_sortie is None else coord_sortie

    def taille_laby(self: Self, laby: List[List[int]]) -> Tuple[int, int]:
        return (len(laby), len(laby[0]))
    
    def voisins_laby_fin(self: Self, lgn: int, col: int, nb_ligne: int, nb_colonne: int) -> List[Tuple[int, int]]:
        voisins: List[Tuple[int, int]] = []

        if lgn > 0:
            voisins.append((lgn - 1, col))
        if lgn < nb_ligne - 1:
            voisins.append((lgn + 1, col))
        if col > 0:
            voisins.append((lgn, col - 1))
        if col < nb_colonne - 1:
            voisins.append((lgn, col + 1))

        return voisins

    def voisins_laby_acc(self: Self, cellule: Tuple[int, int], laby: List[List[int]]) -> List[Tuple[int, int]]:
        taille_laby = self.taille_laby(laby)
        voisins = self.voisins_laby_fin(cellule[0], cellule[1], taille_laby[0], taille_laby[1])
        voisins_acc: List[Tuple[int, int]] = []

        for (i, j) in voisins:
            if laby[i][j] in (self.CHEMIN, self.SORTIE):
                voisins_acc.append((i, j))
        return voisins_acc

    def exploreVoie(self: Self, laby: List[List[int]]) -> List[Tuple[int, int]] | List:
        depart = self.entree(laby)
        arrivee = self.sortie(laby)

        if depart is None or arrivee is None:
            return []

        file = deque([[depart]])
        visitee = set([depart])
        
        while file:
            chemin = file.popleft()
            pos = chemin[-1]

            if pos == arrivee:
                return chemin

            for voisin in self.voisins_laby_acc(pos, laby):
                if voisin not in visitee:
                    visitee.add(voisin)
                    file.append(chemin + [voisin])

        return []
    
    def estMinuscule(self: Self, c: str) -> bool:
        return 'a' <= c <= 'z'

    def decalageCar(self: Self, c: str, decal: int) -> str:
        if self.estMinuscule(c):
            return chr((ord(c) - ord('a') + decal) % 26 + ord('a'))
        else:
            return c
    
    def decalageStr(self: Self, s: str, decal: int) -> str:
        resultat: str = ""
        for c in s:
            resultat += self.decalageCar(c, decal)
        return resultat

    def decalageFichier(self: Self, intext: str, outtext: str, decal: int) -> None:
        with open(intext, 'r', encoding="utf-8") as f:
            contenu: str = f.read()

        contenu_modifie: str = self.decalageStr(contenu, decal)

        with open(outtext, 'w', encoding="utf-8") as fw:
            fw.write(contenu_modifie)

    def resoudre_et_afficher(self: 'TP5', laby: List[List[int]], taille: int = 20) -> None:
        nb_lignes, nb_colonnes = self.taille_laby(laby)
        hauteur = nb_lignes * taille
        largeur = nb_colonnes * taille

        chemin = self.exploreVoie(laby)

        graph.open_win(hauteur, largeur)

        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                y1 = i * taille
                y2 = (i + 1) * taille - 1
                x1 = j * taille
                x2 = (j + 1) * taille - 1

                val = laby[i][j]
                if val == self.MUR:
                    self.tp2.rectangle(y1, y2, x1, x2, "black")
                elif val == self.CHEMIN:
                    self.tp2.rectangle(y1, y2, x1, x2, "white")
                elif val == self.ENTREE:
                    self.tp2.rectangle(y1, y2, x1, x2, "blue")
                elif val == self.SORTIE:
                    self.tp2.rectangle(y1, y2, x1, x2, "red")

        if chemin:
            for (i, j) in chemin:
                y1 = i * taille
                y2 = (i + 1) * taille - 1
                x1 = j * taille
                x2 = (j + 1) * taille - 1
                inset = taille // 6
                self.tp2.rectangle(y1 + inset, y2 - inset, x1 + inset, x2 - inset, "green", False)
        
        graph.wait()
        graph.close()

if __name__ == "__main__":
    x: list = creer(30,30,10)
    tp5: TP5 = TP5()
    tp5.resoudre_et_afficher(x, 20)
