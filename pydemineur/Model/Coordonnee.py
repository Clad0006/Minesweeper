# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(num_ligne:int,num_colonne:int):
    if type(num_ligne)!=int or type(num_colonne)!=int:
        raise TypeError("construireCoordonnee : Le numéro de ligne",type(num_ligne), "ou le numéro de colonne ",type(num_ligne)," ne sontpas des entiers ")
    if num_ligne<0 or num_colonne<0:
        raise ValueError("construireCoordonnee : le numéro de ligne",num_ligne,"ou de colonne",num_colonne,"ne sont pas positifs")
    return (num_ligne,num_colonne)

def getLigneCoordonnee(coordonnees:tuple):
    if type_coordonnee(coordonnees)==False:
        raise TypeError("getLigneCoordonnee : Le paramètre n'est pas une coordonnee")
    return coordonnees[0]

def getColonneCoordonnee(coordonnees:tuple):
    if type_coordonnee(coordonnees)==False:
        raise TypeError("getLigneCoordonnee : Le paramètre n'est pas une coordonnee")
    return coordonnees[1]