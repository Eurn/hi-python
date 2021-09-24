import random
import os


def pickWord():
    choix = []
    file = "words.txt"
    if(os.path.exists(file)):
        dico = open(file, 'r')
        for line in dico.readlines():
            choix.append(line)

        solution = random.choice(choix)
        solution = solution.replace('\n', '')
        return solution
    else:
        print("le fichier contenant les mots n'existe plus ")
        return


def afficheHangman(nb_try):
    if nb_try == 0:
        print(" ==========C= ")
    if nb_try <= 1:
        print(" ||/       |  ")
    if nb_try <= 2:
        print(" ||        O  ")
    if nb_try <= 3:
        print(" ||       /|\ ")
    if nb_try <= 4:
        print(" ||       / \  ")
    if nb_try <= 5:
        print("/||           ")
    if nb_try <= 6:
        print("==============")


def afficheUnderscore(solution):
    affichage = ""
    for i in solution:
        affichage = affichage + "_ "
    return affichage


############################################################################################################
solution = pickWord()
nb_try = 7
letters_find = ""

affichage = afficheUnderscore(solution)
print("Bienvenue dans le jeu du pendu en ANGLAIS!!!")
print(solution)

while nb_try > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")[0:1].lower()
    if ((ord(proposition) >= 65 and ord(proposition) <= 90) or (ord(proposition) >= 97 and ord(proposition) <= 122)):

        if proposition in solution:
            letters_find = letters_find + proposition
            print("Bien jouer, Vous avez trouvé une lettre")
        else:
            nb_try = nb_try - 1
            print("Dommage essayez encore. Il vous reste: " +
                  str(nb_try) + " essais")
            afficheHangman(nb_try)

        affichage = ""
        for x in solution:
            if x in letters_find:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print("   GAGNE!   ")
            break
    else:
        print("ce que vous avez proposé n'est pas une lettre")

print("le mot était: " + solution)
print("\n    Fin de la partie     ")
