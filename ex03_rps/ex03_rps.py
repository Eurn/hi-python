import random


def RockPaperScissors():
    rps = ""
    numGuess = random.randint(1, 3)
    if numGuess == 1:
        rps = "rock"
    elif numGuess == 2:
        rps = "paper"
    else:
        rps = "scissors"
    return rps


def PlayerChoice():
    valide = False
    while not(valide):
        print("Pour choisir la pierre tapez : 1 ou rock")
        print("Pour choisir la feuille tapez : 2 ou paper")
        print("Pour choisir la ciseaux tapez : 3 ou scissors")
        choice = input()
        if choice == "1" or choice == "rock":
            rps = "rock"
            print("Vous avez choisis pierre")
            valide = True
        elif choice == "2" or choice == "paper":
            rps = "paper"
            print("Vous avez choisis feuille")
            valide = True
        elif choice == "3" or choice == "scissors":
            rps = "scissors"
            print("Vous avez choisis ciseaux")
            valide = True
        else:
            print("le choix fait n'est pas valide.")
    return rps


def rejouer():
    yesOrNo = False
    while not(yesOrNo):
        print("Voulez-vous rejouer? oui ou non?")
        choice = input()
        if choice == "oui":
            yesOrNo = True
            return False
        elif choice == "non":
            yesOrNo = True
            return True


playAgain = False
print("Jouons à pierre, feuille, ciseaux.")
while not(playAgain):
    rpsP = PlayerChoice()
    rps = RockPaperScissors()
    if rps == rpsP:
        print("EGALITE")
    elif (rps == 'rock' and rpsP == 'scissors') or (rps == 'paper' and rpsP == 'rock') or (rps == 'scissors' and rpsP == 'paper'):
        print("VOUS AVEZ PERDU. Vous : " + rpsP + " VS, l'odinateur: "+rps)
        playAgain = rejouer()
    else:
        print("VOUS AVEZ GAGNE. Vous : " + rpsP + " VS, l'odinateur: "+rps)
        playAgain = rejouer()
print("Bonne journée")
