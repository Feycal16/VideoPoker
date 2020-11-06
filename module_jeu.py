from collections import Counter
from module_tirage import premier_tirage, deuxieme_tirage
from module_combinaisons import *



def choix_cartes(tirage):
    jeu = []
    for i in tirage:
        print(i)
        choix = input('y/n:')
        if choix == 'y':
            jeu.append(i)
    return jeu #return jeu remis au même niveau que "for" sinon la fonction se termine après la première itération

def choix_carte(chosen_cards):
    new_chosen_cards = []
    count = 0
    for card in chosen_cards:
        #if count < 4:
        print('Voulez vous garder la carte (y/n)? : ' + card)
        user_answer = input()
        if user_answer == 'y':
            #count += 1
            new_chosen_cards.append(card)
    return new_chosen_cards #return jeu remis au même niveau que "for" sinon la fonction se termine après la première itération

def machine():
    deck_initial = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    tirage1, deck = premier_tirage(deck_initial)
    print(tirage1)
    jeu = choix_cartes(tirage1)
    tirage_final = deuxieme_tirage(jeu, deck)
    print(tirage_final)
    return tirage_final

def convert_carte(liste):
    for e,i in zip(liste,range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
               liste[i] = 11
            elif e == 'Q':
               liste[i] = 12
            elif e == 'K':
               liste[i] = 13
            elif e == 'A':
               liste[i] = 1
            else:
               continue        
    return liste

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage,keys):
       dic[k] = i.split('-')
    for key in dic.keys():
       valeur.append(dic[key][0])
       couleur.append(dic[key][1])
    return valeur,couleur    

def calculeJoueur(mise, valeur, couleur):
    valeur = convert_carte(valeur)
    if isQuinteFlushRoyale(valeur, couleur):
        print("Vous avez gagné avec une quinte flush royale, votre gain est de : " + str(mise * 250))
        return mise * 250
    elif isQuinteFlush(valeur, couleur):
        print("Vous avez gagné avec une quinte flush, votre gain est de : " + str(mise * 50))
        return mise * 50
    elif isCarre(valeur):
        print("Vous avez gagné avec un carré, votre gain est de : " + str(mise * 25))
        return mise * 25
    elif isFull(couleur):
        print("Vous avez gagné avec un full, votre gain est de : " + str(mise * 9))
        return mise * 9
    elif isFlush(valeur):
        print("Vous avez gagné avec un flush, votre gain est de : " + str(mise * 6))
        return mise * 6
    elif isQuinte(valeur):
        print("Vous avez gagné avec une quinte, votre gain est de : " + str(mise * 4))
        return mise * 4
    elif isBrelan(valeur):
        print("Vous avez gagné avec un brelan, votre gain est de : " + str(mise * 3))
        return mise * 3
    elif isTwoPair(valeur):
        print("Vous avez gagné avec deux pair, votre gain est de : " + str(mise * 2))
        return mise * 2
    elif isPair(valeur):
        print("Vous avez gagné avec une pair, votre gain est de : " + str(mise))
        return mise
    else:
        print("Vous n'avez gagné !")
        return 0

def partie(mise, bankroll):
    tirage = machine()
    print("machine",tirage)
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    return bankroll + calculeJoueur(mise, valeur, couleur)    