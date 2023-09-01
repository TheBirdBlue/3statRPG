import random
import time
import common

# # # FOR TESTING PURPOSES # # #
playerStats = ['TEST', 10, 3, 3, 3, 0]
enemyStats = ['Slime Rat', 5, 2]

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
playerCurrent = [playerHPCurrent, playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent]

enemyName = enemyStats[0]
enemyHPMax = enemyStats[1]
enemyAttacksMax = enemyStats[2]
enemyHPCurrent = enemyHPMax
enemyAttacksCurrent = enemyAttacksMax
# # # END TESTING DATA # # #

unused = '⦿'
used = '○'

def drawUI(playerBase, playerCurrent, enemyBase, eemyCurrent):
    # Set up common name variables for player
    playerName = playerBase[0]
    playerHPMax = playerBase[1]
    playerStrengthMax = playerBase[2]
    playerMagicMax = playerBase[3]
    playerSkillMax = playerBase[4]
    playerHPCurrent = playerCurrent[0]
    playerStrengthCurrent = playerCurrent[1]
    playerMagicCurrent = playerCurrent[2]
    playerSkillCurrent = playerCurrent[3]

    # Set up common name variables for enemy
    enemyName = enemyStats[0]
    enemyHPMax = enemyStats[1]
    enemyAttacksMax = enemyStats[2]
    enemyHPCurrent = enemyHPMax
    enemyAttacksCurrent = enemyAttacksMax

    # Calculate HP percents
    playerHPPercent = int((playerHPCurrent / playerHPMax) * 15)
    enemyHPPercent = int((enemyHPCurrent / enemyHPMax) * 21)

    # Check if player and enemy have more than 1 HP but percent calculation gives 0
    if playerHPPercent == 0 or enemyHPPercent == 0:
        if playerHPCurrent >= 1:
            playerHPPercent = 1
        if enemyHPCurrent >= 1:
            enemyHPPercent = 1

    # Set template for printing
    playerHPDisplay = str(playerHPCurrent) + ' / ' + str(playerHPMax)
    lengthInsert = 16 + len(playerHPDisplay)

    # Moves enemy bar to better align with player bar
    enemyLineZero = ' ' * lengthInsert + '{:>23}'
    enemyLineOne = ' ' * (lengthInsert - 1) + ' ║ [{:>21}] ║'
    enemyLineTwo = ' ' * lengthInsert + '╚' + '═' * (lengthInsert + 2) + '╝'

    # Sets lengths on player display to match with longer numbers
    length = "{:>" + str(lengthInsert - 16) + "}"
    playerLineData = ' ║ [{:<15}] ' + '{}' + length + ' ║'
    playerLineBottom = ' ╚' + '═' * (lengthInsert + 7) + '╝'
    playerLineAction = ' ║ {:3} ║ {:' + str(lengthInsert - 1) + '} ║'


    # Prints bars for display
    print(enemyLineZero.format(enemyName))
    print(enemyLineOne.format('▓' * enemyHPPercent))
    print(enemyLineTwo, '\n')
    print(playerLineData.format('▓' * playerHPPercent, 'HP ', playerHPDisplay))

    # Set up and create lines for actions
    current = [playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent]
    maximum = [playerStrengthMax, playerMagicMax, playerSkillMax]
    skillName = ['STR', 'MAG', 'SKL']
    for skill, curr, max in zip(skillName, current, maximum):
        unusedAmount = curr
        usedAmount = max - curr
        actionDisplay = (unused * unusedAmount) + (used * usedAmount)
        print(playerLineAction.format(skill, actionDisplay))
    print(playerLineBottom)

def takeAction(action, playerItemsBase, playerItemsMax, enemyItems):
    if action == 'Strength':
        if playerItemsBase[0] == playerItemsMax[0]:
        attackLineSetup = ' You have {} rolls available [{} damage].\n How many would you like to use? '
        damageRange = str(playerItemsBase[0] * 1) + ' - ' + str(playerItemsMax[0] * 6)
        playerChoice = input(attackLineSetup.format(playerItemsBase[0], damageRange))

    # For the rest action
    else:
        recoveryRead = []
        for stat, limit in zip(playerItemsBase, playerItemsMax):

            # Ensures that recovery does not exceed maximum
            if stat + 1 > limit:
                stat = limit
                recoveryRead.append(0)
            else:
                stat += 1
                recoveryRead.append(1)

        # Changes health recovery from base to percentage
        maxDifference = playerItemsMax[3] - playerItemsBase[3]
        healthRecover = int(playerItemsMax[3] * 0.2)
        playerItemsBase[3] += healthRecover
        recoveryRead[3] = healthRecover
        if playerItemsBase[3] > playerItemsMax[3]:
            recoveryRead[3] = maxDifference
            playerItemsBase[3] = playerItemsMax[3]


        recoveryLine = ' Recovered {} strength, {} magic, {} skill, and {} HP.'
        print(recoveryLine.format(recoveryRead[0], recoveryRead[1], recoveryRead[2], recoveryRead[3]))
        time.sleep(2)

def battleStart(playerBase, playerCurrent, enemyBase):

    # Set up common name variables for player
    playerName = playerBase[0]
    playerHPMax = playerBase[1]
    playerStrengthMax = playerBase[2]
    playerMagicMax = playerBase[3]
    playerSkillMax = playerBase[4]
    playerHPCurrent = playerCurrent[0]
    playerStrengthCurrent = int(playerCurrent[1])
    playerMagicCurrent = int(playerCurrent[2])
    playerSkillCurrent = int(playerCurrent[3])

    # Set up common name variables for enemy
    enemyName = enemyStats[0]
    enemyHPMax = enemyStats[1]
    enemyAttacksMax = enemyStats[2]
    enemyHPCurrent = enemyHPMax
    enemyAttacksCurrent = enemyAttacksMax

    enemyCurrent = [enemyHPCurrent, enemyAttacksCurrent]
    playerStrength = [playerStrengthCurrent, playerHPCurrent]
    playerStrengthLimit = [playerStrengthMax, playerHPMax]
    playerMagic = [playerMagicCurrent, playerHPCurrent]
    playerMagicLimit = [playerMagicMax, playerHPMax]
    playerSkill = [playerSkillCurrent, playerHPCurrent]
    playerSkillLimit = [playerSkillMax, playerHPMax]
    playerRest = [playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent, playerHPCurrent]
    playerRestLimit = [playerStrengthMax, playerMagicMax, playerSkillMax, playerHPMax]

    common.clear()
    battlestate = True
    while battlestate:
        drawUI(playerBase, playerCurrent, enemyBase, enemyCurrent)

        # Check is player can take an action. If unable, forces rest action for the turn
        if playerStrengthCurrent and playerMagicCurrent and playerSkillCurrent < 0:
            print(" You have to take a rest action.")
            time.sleep(2)
            playerActionList = takeAction(playerRest, enemyCurrent)

        # If player can take action, allows player to choose and fight
        else:

            print('\n What action will you roll?')
            playerAction = input(' (S)TR | (M)AG | S(K)L | (R)est\n Action: ')
            playerAction = playerAction.lower()

            if playerAction == 's':
                if playerStrengthCurrent < 1:
                    print(" You don't have enough strength left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Strength', playerStrength, playerStrengthLimit, enemyCurrent)
                    playerStrengthCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'm':
                if playerMagicCurrent < 1:
                    print(" You don't have enough magic left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Magic', playerMagic, playerMagicLimit, enemyCurrent)
                    playerMagicCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'k':
                if playerMagicCurrent < 1:
                    print(" You don't have enough skill left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Skill', playerSkill, playerSkillLimit, enemyCurrent)
                    playerMagicCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'r':
                playerActionList = takeAction('Rest', playerRest, playerRestLimit, enemyCurrent)

            else:
                print(' Invalid action. Please try again.')
                time.sleep(2)


battleStart(playerBase, playerCurrent, enemyStats)