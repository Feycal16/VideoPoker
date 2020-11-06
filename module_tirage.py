import random

def premier_tirage(deck):
    tirage = random.sample(deck,5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck

#pt = premier_tirage(deck)

def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    carte_a_tirer = 5 - nb_carte
    nouvelle_carte = random.sample(deck, carte_a_tirer)
    for i in nouvelle_carte:
        jeu.append(i)
    return jeu #return jeu remis au même niveau que "for" sinon la fonction se termine après la première itération