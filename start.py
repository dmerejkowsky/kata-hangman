import random


def lire_mots():
    fichier = open("mots.txt")
    contenu = fichier.read()
    fichier.close()
    mots = contenu.splitlines()
    return mots


def choisir_mot_au_hasard(mots):
    taille = len(mots)
    index = random.randint(0, taille)
    return mots[0]


def jouer():
    mots = lire_mots()
    mot = choisir_mot_au_hasard(mots)
    # pour débugger, il faudra enlever cet
    # appel à print une fois le code terminé
    print("Le mot à deviner est", mot)
    tentatives = []
    while True:
        afficher_indice(mot, tentatives)
        lettre = demander_lettre()
        if lettre not in tentatives:
            tentatives += [lettre]
        if a_gagné(mot, tentatives):
            print(mot)
            print("Gagné")
            break


def a_gagné(mot, tentatives):
    return False


def demander_lettre():
    print("entrer une lettre")
    lettre = input()
    return lettre


def afficher_indice(mot, tentatives):
    print("tentatives", tentatives)


jouer()
