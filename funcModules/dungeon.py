import common
import time
import random
import smallDungeons as sdm
import mediumDungeons as mdm
import largeDungeons as ldm
import extremeDungeons as edm
import battleFunction

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
    exit = False
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

        playerBase = [playerHPMax, playerStrengthMax, playerMagicMax, playerSkillMax]
        playerCurrent = [playerHPCurrent, playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent, playerExp]

        noEnemy = ['none', 1, 1]
        common.clear()
        printMap(dungeonDict, playerPosition)
        battleFunction.drawUI(playerBase, playerCurrent, noEnemy, noEnemy)

        # Checks is in exit room
        if currentRoom['x'] == dungeonDict['exit']['x'] and currentRoom['y'] == dungeonDict['exit']['y']:
            exit = True
            print(" There's the exit!")
            time.sleep(2)
        else:
            exit = False

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
        if exit:
            print('\n   Fight    ▲    Rest\n'
                  '         7  8  9 \n'
                  '       ◄ 4  ■  6 ►\n'
                  '         1  2  3 \n'
                  '     Exit   ▼    Retreat\n')

        else:
            print('\n   Fight    ▲    Rest\n'
                  '         7  8  9 \n'
                  '       ◄ 4  ■  6 ►\n'
                  '         1  2  3 \n'
                  '            ▼    Retreat\n')

        print(' DEBUG\n', currentRoom, '\n ln-129')

        playerInput = input(' Select and action:  ')

        #try:
        playerInput = int(playerInput)

        # Fight action
        if playerInput == 7:
            if 7 in currentRoom['action']:
                print(' You have already cleared this room.')
                time.sleep(2)
            else:
                workingList = battleFunction.battleStart(playerBase, playerCurrent, rank)
                print(workingList, 'ln-183')
                playerHPCurrent = workingList[0]
                playerStrengthCurrent = workingList[1]
                playerMagicCurrent = workingList[2]
                playerSkillCurrent = workingList[3]
                playerExp = workingList[4]
                currentRoom['action'].append(7)

        # Rest actions
        if playerInput == 1:
            if 7 in currentRoom['action'] and exit:
                playerConfirmation = input(' Do you want to exit (Y or N)?  ')
                if playerConfirmation.lower() == 'y':
                    runDungeon = False
                    playerExp += len(dungeonDict) * rank
            else:
                pass


        if playerInput == 3:
            playerConfirmation = input(' Are you sure you want to leave (Y or N)?  ')
            playerConfirmation = playerConfirmation.lower()
            if playerConfirmation == 'y':
                runDungeon = False
            else:
                print(' Continue pressing on.')
                time.sleep(2)

        if playerInput == 9:
            if 7 in currentRoom['action']:
                if 9 not in currentRoom['action']:
                    currentRoom['action'].append(9)

                    # For HP recovery
                    playerHPCurrent += int(playerHPMax * 1.2)
                    if playerHPCurrent > playerHPMax:
                        playerHPCurrent = playerHPMax

                    # For strength recovery
                    playerStrengthCurrent += int(playerStrengthMax * 0.34)
                    if playerStrengthCurrent > playerStrengthMax:
                        playerStrengthCurrent = playerStrengthMax

                    # For magic recovery
                    playerMagicCurrent += int(playerMagicMax * 0.34)
                    if playerMagicCurrent > playerMagicMax:
                        playerMagicCurrent = playerMagicMax

                    # For skill recovery
                    playerSkillCurrent += int(playerSkillMax * 0.34)
                    if playerSkillCurrent > playerSkillMax:
                        playerSkillCurrent = playerSkillMax

                    restAction = False
                else:
                    print(' You have already rested here. Time to move on.')
                    time.sleep(2)
            else:
                print(" It's not safe to rest here.")
                time.sleep(2)

        # Move actions
        if playerInput == 8:
            if 7 not in currentRoom['action']:
                print(' You are unable to move with an enemy in the room.')
                time.sleep(2)
            else:
                workingList = moveAction(currentRoom, dungeonDict, playerPosition, 0)
                currentRoom =workingList[0]
                playerPosition = workingList[1]

        if playerInput == 6:
            if 7 not in currentRoom['action']:
                print(' You are unable to move with an enemy in the room.')
                time.sleep(2)
            else:
                workingList = moveAction(currentRoom, dungeonDict, playerPosition, 1)
                currentRoom =workingList[0]
                playerPosition = workingList[1]

        if playerInput == 2:
            if 7 not in currentRoom['action']:
                print(' You are unable to move with an enemy in the room.')
                time.sleep(2)
            else:
                workingList = moveAction(currentRoom, dungeonDict, playerPosition, 2)
                currentRoom =workingList[0]
                playerPosition = workingList[1]

        if playerInput == 4:
            if 7 not in currentRoom['action']:
                print(' You are unable to move with an enemy in the room.')
                time.sleep(2)
            else:
                workingList = moveAction(currentRoom, dungeonDict, playerPosition, 3)
                currentRoom =workingList[0]
                playerPosition = workingList[1]

        if playerHPCurrent <= 0:
            print(' That is all for this run. Returning to home...')
            time.sleep(5)
            runDungeon = False

        #except:
        #    print(' Invalid input.')

    return playerExp

def moveAction(room, dungeon, playerPosition, action):

    if room['direction'][action] == 1:
        queuedRoom = room['room'][action]
        room = dungeon[queuedRoom]
        playerPosition = [room['x'], room['y']]

        print(room, playerPosition, 'ln-265')
        return room, playerPosition
    else:
        print(' You cannot move that way.')
        time.sleep(2)
        return room, playerPosition

def dungeonMainMenu(playerStats):
    playerName = playerStats[0]
    playerHPMax = playerStats[1]
    playerStrength = playerStats[2]
    playerMagic = playerStats[3]
    playerSkill = playerStats[4]
    playerExp = playerStats[5]

    options = ['New Dungeon', 'Change Rank', 'Return']

    dungeonMenu = True
    rank = 1

    while dungeonMenu:
        common.runUI(playerStats, playerHPMax, options)

        playerChoice = input(' Please make a selection:  ')
        playerChoice = int(playerChoice)
        if playerChoice == 1:
            print('\n (S)mall - 4 to 10 rooms'
                  '\n (M)edium - 11 to 20 rooms'
                  '\n (L)arge - 21 to 40 rooms'
                  '\n (E)xtreme - 50 to 75 rooms')
            size = input('\n What size dungeon would you like to enter?  ')
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

            experienceReturn = dungeonRun(playerStats, rank, size)
            playerStats[5] = experienceReturn


        if playerChoice == 2:
            playerInput = input(' What rank would you like to delve at?  ')
            try:
                playerInput = int(playerInput)
                rank = playerInput
            except:
                print(' Invalid input.')
                time.sleep(2)

        if playerChoice == 3:
            dungeonMenu = False
            return playerStats

#playerStats = ['TEST', 10, 3, 3, 3, 0]
#rank = 1
#size = 'sdm'
#dungeonRun(playerStats, rank, size)
