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

def construireGrilleDemineur(l:int,c:int)->list:
    grille=[]
    if l<=0 or c<=0:
        raise ValueError("construireGrilleDemineur : Le nombre de lignes",l," ou de colonnes",c," est négatif ou nul.")
    else:
        for i in range(l):
            ligne=[]
            for i in range(c):
                cell=construireCellule(0,False)
                ligne.append(cell)
            grille.append(ligne)
    return grille

def getNbLignesGrilleDemineur(grille:list)->int:
    if type_grille_demineur(grille)==False:
        raise TypeError("« getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille:list)->int:
    if type_grille_demineur(grille)==False:
        raise TypeError("« getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille:list,coord:tuple)-> bool:
    if type_grille_demineur(grille)==False or type_coordonnee(coord)==False :
        raise TypeError("isCoordonneeCorrecte : un des paramètres n'est pas du bon type")
    res=False
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if (i,j)==coord:
                res=True
    return res

def getCelluleGrilleDemineur(grille:list,coord:tuple)->dict:
    if type_grille_demineur(grille)==False or type_coordonnee(coord)==False :
        raise TypeError("isCoordonneeCorrecte : un des paramètres n'est pas du bon type")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coord[0]][coord[1]]