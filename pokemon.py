# Pokemon class, name, stats types
# Moves
# Read in cvs
# Randomly choose two pokemon


# Display text, hp, attacks
# You win if destroy pokemon
# lvl 100

import pandas as pd
import random

class Pokemon:
    def __init__(self, name=None, type1=None, hp=None, maxHp=None, attack=None, defense=None):
        self.name = name
        self.type1 = type1
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack * 0.2
        self.defense = defense

# main
pFile = pd.read_csv('gen01.csv')
playerPID = random.randint(1, 151)
playerPType = pFile.loc[playerPID, 'Type1']
enemyPID = random.randint(1, 151)
enemyPType = pFile.loc[enemyPID, 'Type1']
while playerPType != 'Grass' and playerPType != 'Fire' and playerPType != 'Water':
    playerPID = random.randint(0, 150)
    playerPType = pFile.loc[playerPID, 'Type1']

while enemyPType != 'Grass' and enemyPType != 'Water' and enemyPType != 'Fire':
    enemyPID = random.randint(0, 150)
    enemyPType = pFile.loc[enemyPID, 'Type1']

playerP = Pokemon(pFile.loc[playerPID, 'Name'],
                  pFile.loc[playerPID, 'Type1'],
                  pFile.loc[playerPID, 'HP'],
                  pFile.loc[playerPID, 'HP'],
                  pFile.loc[playerPID, 'Attack'],
                  pFile.loc[playerPID, 'Defense']
                  )

enemyP = Pokemon(pFile.loc[enemyPID, 'Name'],
                  pFile.loc[enemyPID, 'Type1'],
                  pFile.loc[enemyPID, 'HP'],
                  pFile.loc[enemyPID, 'HP'],
                  pFile.loc[enemyPID, 'Attack'],
                  pFile.loc[enemyPID, 'Defense']
                  )

def printGame():
    if(enemyP.hp <= 0 or playerP.hp <= 0):
        return False

    print("Your pokemon", playerP.name, "HP: ", round(playerP.hp))
    print("Your enemy", enemyP.name, "HP: ", round(enemyP.hp))
    choice = input("Attack (a), Heal (h), Defend (d), Exit(e): ")
    print()
    while handleChoice(choice):
        print()
    

def handleChoice(choice):
    if(choice != 'a' and choice != 'h' and choice != 'd' and choice != 'e'):
        printGame()
    elif choice == 'e':
        print("Exiting...")
        playerP.hp = 0
        enemyP.hp = 0
        return
    elif choice == 'a':
        enemyP.hp -= playerP.attack
        print("You did ", round(playerP.attack), " dmg")
        if(enemyP.hp <= 0):
            return False
        playerP.hp -= enemyP.attack
        print("Enemy did ", round(enemyP.attack), " dmg")
        if(playerP.hp <= 0):
            return False
    elif choice == 'h':
        playerP.hp += playerP.hp * 0.3
        if(playerP.hp > playerP.hp):
            playerP.hp = playerP.hp 
    elif choice == 'd':
        playerP.hp -= enemyP.attack * 0.9
        print("You defended")
        print("Enemy did ", round(enemyP.attack * 0.9), " dmg")
        if(playerP.hp <= 0):
            return False
    print()
    print()
    print()
print("Chopped pokemon showdown")

while(playerP.hp > 0 and enemyP.hp > 0):
    printGame()

if(enemyP.hp <= 0):
    print("You win")
elif(playerP.hp <= 0):
    print("You Lost bozo")