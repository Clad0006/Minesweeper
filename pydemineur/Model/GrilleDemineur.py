# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                                         and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(l: int, c: int) -> list:
    grille = []
    if l <= 0 or c <= 0:
        raise ValueError("construireGrilleDemineur : Le nombre de lignes", l, " ou de colonnes", c,
                         " est négatif ou nul.")
    else:
        for i in range(l):
            ligne = []
            for i in range(c):
                cell = construireCellule(0, False)
                ligne.append(cell)
            grille.append(ligne)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("« getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise TypeError("« getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n'est pas du bon type")
    res = False
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if (i, j) == coord:
                res = True
    return res


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n'est pas du bon type")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return grille[coord[0]][coord[1]][const.CONTENU]


def setContenuGrilleDemineur(grille: list, coord: tuple, n: int) -> None:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False or type(n) != int:
        raise TypeError("SetContenuGrilleDemineur : Le type de l'un ds coordonnées n'est pas correct")
    if ((0 > n or n > 8) and n != const.ID_MINE) and type(n) == int:
        raise ValueError("construireCellule : le contenu", n, "n'est pas valide")
    grille[coord[0]][coord[1]][const.CONTENU] = n
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return grille[coord[0]][coord[1]][const.VISIBLE]


def setVisibleGrilleDemineur(grille: list, coord: tuple, b: bool) -> None:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False or type(b) != bool:
        raise TypeError("SetContenuGrilleDemineur : Le type de l'un ds coordonnées n'est pas correct")
    grille[coord[0]][coord[1]][const.VISIBLE] = b
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    res = False
    if grille[coord[0]][coord[1]][const.CONTENU] == const.ID_MINE:
        res = True
    return res


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    if type_grille_demineur(grille) == False or type_coordonnee(coord) == False:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des deux paramètres n'a pas le bon type")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnee n'est pas contenue dans la grille")
    res = []
    if 0 <= coord[0] - 1 < len(grille) and 0 <= coord[1] < len(grille[0]):
        res.append((coord[0] - 1, coord[1]))
    if 0 <= coord[0] < len(grille) and 0 <= coord[1] - 1 < len(grille[0]):
        res.append((coord[0], coord[1] - 1))
    if 0 <= coord[0] + 1 < len(grille) and 0 <= coord[1] < len(grille[0]):
        res.append((coord[0] + 1, coord[1]))
    if 0 <= coord[0] < len(grille) and 0 <= coord[1] + 1 < len(grille[0]):
        res.append((coord[0], coord[1] + 1))
    if 0 <= coord[0] - 1 < len(grille) and 0 <= coord[1] - 1 < len(grille[0]):
        res.append((coord[0] - 1, coord[1] - 1))
    if 0 <= coord[0] + 1 < len(grille) and 0 <= coord[1] + 1 < len(grille[0]):
        res.append((coord[0] + 1, coord[1] + 1))
    if 0 <= coord[0] - 1 < len(grille) and 0 <= coord[1] + 1 < len(grille[0]):
        res.append((coord[0] - 1, coord[1] + 1))
    if 0 <= coord[0] + 1 < len(grille) and 0 <= coord[1] - 1 < len(grille[0]):
        res.append((coord[0] + 1, coord[1] - 1))
    return res


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    if nb < 0 or nb > (len(grille[0]) * len(grille) - 1):
        raise ValueError("placerMinesGrilleDemineur : Nombre de mines a placer incorrect")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("placerMinesGrilleDemineur : La coordonnee n'est pas dans la grille")
    i = 0
    while i < nb:
        a = randint(0, len(grille) - 1)
        b = randint(0, len(grille[0]) - 1)
        if (a, b) != coord and grille[a][b][const.CONTENU] != const.ID_MINE:
            setContenuCellule(grille[a][b], const.ID_MINE)
            i += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            mines = 0
            if grille[i][j][const.CONTENU] != const.ID_MINE:
                coord = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                for k in coord:
                    if contientMineGrilleDemineur(grille, k):
                        mines += 1
                grille[i][j][const.CONTENU] = mines
    return None

def getNbMinesGrilleDemineur(grille:list)->int:
    if type_grille_demineur(grille)==False:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n'est pas une grille")
    res=0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j][const.CONTENU] == const.ID_MINE:
                res+=1
    return res

def getAnnotationGrilleDemineur(grille:list,coord:tuple)->str:
    return grille[coord[0]][coord[1]][const.ANNOTATION]