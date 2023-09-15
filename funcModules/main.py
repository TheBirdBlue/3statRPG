#!/usr/bin/python

import time
import os
import sys

sys.path.insert(0, './funcModules')
sys.path.insert(1, './funcModules/dungeons')
sys.path.insert(2, './saves')

import common
import saveload
import dungeon

# Initialize global variables
run = True
playerStats = ['', 10, 3, 3, 3, 0]
enemystats = ['Slime Rat', 5, 2]

# Common names
playerName = playerStats[0]
playerHPMax = playerStats[1]
playerStrength = playerStats[2]
playerMagic = playerStats[3]
playerSkill = playerStats[4]
playerExp = playerStats[5]
enemyName = [0]
enemyHP = enemystats[1]
enemyAttacks = enemystats[2]

# Player save variables
fileLocationPlayer = './saves'
loadNames = []

# Options List
options = ['Enter a Dungeon', 'Go to Training', 'Shop', 'Exit']

def main():
    print(' Select enter a save name or enter a new name to create a new save;')
    loadNames = os.listdir('./saves')
    position = 1
    for names in loadNames:
        print('   ' + str(position), ' - ', names)
        position += 1
    name = input(" Select save:  ")
    if name in loadNames:
        playerStats = saveload.loadPlayer(name)
        playerCurrentHP = playerStats[1]
    else:
        playerStats = saveload.createPlayer(name)
        playerCurrentHP = playerStats[1]

    while run:
        common.runUI(playerStats, playerCurrentHP, options)

        playerInput = input(' Select an option: ')
        #try:
        playerInput = int(playerInput)
        if playerInput == 1:
            playerStats = dungeon.dungeonMainMenu(playerStats)
            saveload.savePlayer(playerStats)
        #except:
        #    print(' Invalid input.')
        #    time.sleep(2)

main()
