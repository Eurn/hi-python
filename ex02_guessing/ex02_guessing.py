import random


def RandRange():
    print("donnez le nombre min")
    minRange = int(input())
    print("donnez le nombre max")
    maxRange = int(input())

    numGuess = random.randint(minRange, maxRange)
    print("le système a choisit un nombre aléatoire entre " +
          str(minRange)+" et "+str(maxRange)+" compris, à vous de le deviner!")
    return numGuess


def PlayerChoice(numGuess):
    choiceIsGuess = False
    while not(choiceIsGuess):
        choice = int(input())
        if choice > numGuess:
            print("le nombre est inférieur à celui entré")
        elif choice < numGuess:
            print("le nombre est supérieur à celui entré")
        else:
            print("BRAVO VOUS AVEZ TOUVEZ!")
            choiceIsGuess = True
    return


numGuess = RandRange()
PlayerChoice(numGuess)
