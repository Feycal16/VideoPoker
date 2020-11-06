from collections import Counter

def isPair(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 2:
            return True
    return False

def isTwoPair(valeur):
    cpt = 0
    counter = Counter(valeur)
    for i in counter.values():
        if i == 2:
            cpt += 1
    
    if cpt == 2:
        return True
    else:
        return False

def isBrelan(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 3:
            return True
    return False

def isQuinte(valeur):
    liste = sorted(valeur)
    if liste[0] + 4 == liste[4]:
        return True
    else:
        return False

def isFlush(couleur):
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False

def isFull(valeur):
    if (isPair(valeur) and isBrelan(valeur)):
        return True
    else:
        return False

def isCarre(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 4:
            return True
    return False

def isQuinteFlush(valeur, couleur):
    if isQuinte(valeur) and isFlush(couleur):
        return True
    else:
        return False

def isQuinteFlushRoyale(valeur, couleur):
    if isQuinteFlush(valeur, couleur) and valeur == [10, 11, 12, 13, 14]:
        return True
    else:
        return False