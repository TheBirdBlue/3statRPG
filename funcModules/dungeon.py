import common
import time
import random
import smallDungeons as sdm
import mediumDungeons as mdm
import largeDungeons as ldm
import extremeDungeons as edm

debugLine = ' xRange: {}, Room: {}, x: {}, y: {}'
roomEmpty = '☐'
roomFull = '☒'

def printMap(dungeonDict, playerLocation):
    topLine = '\n ╔ {}╗'
    printLine = ' ║ {}║'
    bottomLine = ' ╚ {}╝'

    # Find max height and length
    xHeight = 0
    yLength = 0
    for room in dungeonDict:
        if dungeonDict[room]['x'] > xHeight:
            xHeight = dungeonDict[room]['x']
        if dungeonDict[room]['y'] > yLength:
            yLength = dungeonDict[room]['y']

    # Print top line and format map lines
    print(topLine.format('= ' * (yLength + 1)))

    # Begin going through all lines
    for xRange in range(0, xHeight + 1):
        thisLine = []

        # Go through room by room to check if room is on that line
        for room in dungeonDict:

            # Add room on the same line to list
            if dungeonDict[room]['x'] == xRange:
                coordinates = dungeonDict[room]['y']
                thisLine.append(coordinates)

        # Begin creating that line by building blank list with correct spaces
        lineList = []
        for x in range(0, yLength + 1):
            lineList.append(' ')

        for space in lineList:
            for location in thisLine:
                lineList[location] = roomEmpty

        # Checks if player is on the same line
        if playerLocation[0] == xRange:
            lineList[playerLocation[1]] = roomFull

        stringLine = ''
        for item in lineList:
            stringLine += item + ' '
        print(printLine.format(stringLine))

    print(bottomLine.format('= ' * (yLength + 1)), '\n')

def dungeonRun(playerStats, rank, size):
    runDungeon = True
    playerName = playerStats[0]
    playerHPMax = playerStats[1]
    playerStrengthMax = playerStats[2]
    playerMagicMax = playerStats[3]
    playerSkillMax = playerStats[4]
    playerExp = playerStats[5]
    playerHPCurrent = playerHPMax
    playerStrengthCurrent = playerStrengthMax
    playerMagicCurrent = playerMagicMax
    playerSkillCurrent = playerSkillMax

    playerBase = [playerName, playerHPMax, playerStrengthMax, playerMagicMax, playerSkillMax]
    playerCurrent = [playerName, playerHPCurrent, playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent]

    # Pull Dungeon
    if size == 'sdm':
        dungeonList = sdm.list
    elif size == 'mdm':
        dungeonList = mdm.list
    elif size == 'ldm':
        dungeonList = ldm.list
    elif size == 'edm':
        dungeonList = edm.list

    dungeonSelection = random.randrange(0, len(dungeonList))
    dungeonDict = dungeonList[dungeonSelection]

    # Set player starting position
    playerPositionX = dungeonDict['room0']['x']
    playerPositionY = dungeonDict['room0']['y']
    playerPosition = [playerPositionX, playerPositionY]
    currentRoom = dungeonDict['room0']

    while runDungeon:

        common.clear()
        printMap(dungeonDict, playerPosition)

        # Present the player with the room status and actions available
        roomStatus = ' You have {}taken the {} action.'
        if 7 not in currentRoom['action']:
            print(roomStatus.format('NOT ', 'fight'))
        else:
            print(roomStatus.format('', 'fight'))

        if 1 and 3 and 9 not in currentRoom['action']:
            print(roomStatus.format('NOT ', 'rest'))
        else:
            print(roomStatus.format('', 'rest'))

        # Movement and action UI
        print('   Fight    ▲    Rest\n'
              '         7  8  9 \n'
              '       ◄ 4  ■  6 ►\n'
              '         1  2  3 \n'
              ' Stretch    ▼    Focus\n')
        playerInput = input(' Select and action: ')

        #try:
        playerInput = int(playerInput)

        # Stretch Action
        if 7 in currentRoom['action']:
            restAction = True
        else:
            restAction = False

        # Rest actions
        if playerInput == 1:
            if restAction and 1 or 3 or 9 not in currentRoom['action']:
                currentRoom['action'].append(1)
                playerHPCurrent += int(playerHPMax * 1.2)
                if playerHPCurrent > playerHPMax:
                    playerHPCurrent = playerHPMax
                playerStrengthCurrent += int(playerStrengthMax * 1.33)
                if playerStrengthCurrent > playerStrengthMax:
                    playerStrengthCurrent = playerStrengthMax
            else:
                print(" It's not safe to rest here.")
                time.sleep(2)

        if playerInput == 3:
            if restAction and 1 or 3 or 9 not in currentRoom['action']:
                currentRoom['action'].append(3)
                playerHPCurrent += int(playerHPMax * 1.2)
                if playerHPCurrent > playerHPMax:
                    playerHPCurrent = playerHPMax
                playerMagicCurrent += int(playerMagicMax * 1.33)
                if playerMagicCurrent > playerMagicMax:
                    playerMagicCurrent = playerMagicMax
            else:
                print(" It's not safe to rest here.")
                time.sleep(2)

        if playerInput == 7:
            if 7 in currentRoom['action']:
                print(' You have already cleared this room.')
                time.sleep(2)
            else:
                pass

        if playerInput == 9:
            if restAction and 1 or 3 or 9 not in currentRoom['action']:
                currentRoom['action'].append(9)
                playerHPCurrent += int(playerHPMax * 1.2)
                if playerHPCurrent > playerHPMax:
                    playerHPCurrent = playerHPMax
                playerSkillCurrent += int(playerSkillMax * 1.33)
                if playerSkillCurrent > playerSkillMax:
                    playerSkillCurrent = playerSkillMax
            else:
                print(" It's not safe to rest here.")
                time.sleep(2)

        #except:
        #    print(' Invalid input.')
        runDungeon = False

def dungeonMainMenu(playerStats):
    playerName = playerStats[0]
    playerHPMax = playerStats[1]
    playerStrength = playerStats[2]
    playerMagic = playerStats[3]
    playerSkill = playerStats[4]
    playerExp = playerStats[5]

    options = ['New Dungeon', 'Change Rank', 'Return']

    dungeonMenu = True

    while dungeonMenu:
        common.runUI(playerStats, playerHPMax, options)

        playerChoice = input(' Press enter to continue...')
        playerChoice = int(playerChoice)
        if playerChoice == 1:
            print('\n (S)mall - 4 to 10 rooms'
                  '\n (M)edium - 11 to 20 rooms'
                  '\n (L)arge - 21 to 40 rooms'
                  '\n (E)xtreme - 50 to 75 rooms')
            size = input('\n What size dungeon would you like to enter?')
            if size == 'S' or 's':
                size = 'sdm'
            elif size == 'M' or 'm':
                size = 'mdm'
            elif size == 'L' or 'l':
                size = 'ldm'
            elif size == 'E' or 'e':
                size = 'edm'
            else:
                print(' Invalid size selection.')

            dungeonRun(playerStats, 1, size)


'''
        for dicts in dir(smallDungeons):
            if '__' in dicts:
                pass
            else:
                print(dicts)
'''
