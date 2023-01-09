# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(n:int)->bool:
    res=False
    if type(n)==int and (0<=n<=8 or n==const.ID_MINE)  :
        res=True
    return res

def construireCellule(n:int=0,visible:bool=False)->dict:
    if ((0 > n or n> 8) and n != const.ID_MINE) and type(n) == int:
        raise ValueError("construireCellule : le contenu",n,"n'est pas valide")
    if type(visible)!=bool:
        raise TypeError("construireCellule : le second paramètre",visible,"n'est pas un booleen")
    cellule={const.CONTENU:n,const.VISIBLE:visible}
    return cellule

def getContenuCellule(cell:dict)->int:
    return cell[const.CONTENU]

def isVisibleCellule(cell:dict)->bool:
    return cell[const.VISIBLE]

def setContenuCellule(cell:dict,n:int)->None:
    if type_cellule(cell)==False:
        raise TypeError("setContenuCellule : le premier paramètre n'est pas une cellule")
    if type(n)!=int:
        raise TypeError("setContenuCellule : Le second paramètre n'est pas un entier")
    if isContenuCorrect(n)==False:
        raise ValueError("setContenuCellule : la valeur du contenu",n, "n’est pas correcte.")
    cell[const.CONTENU]=n
    return None

def setVisibleCellule(cell:dict,b:bool)->None:
    cell[const.VISIBLE]=b
    return None

def contientMineCellule(cell:dict)->bool:
    res=False
    if cell[const.CONTENU]==const.ID_MINE:
        res=True
    return res