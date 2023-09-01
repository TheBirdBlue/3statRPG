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

def drawUI(playerBase, playerCurrent, enemyBase, enemyCurrent):
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
    enemyName = enemyBase[0]
    enemyHPMax = enemyBase[1]
    enemyAttacksMax = enemyBase[2]
    enemyHPCurrent = enemyCurrent[1]
    enemyAttacksCurrent = enemyCurrent[2]

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

def takeAction(action, playerItemsBase, playerItemsMax, enemyItemsBase, enemyItemsMax):

    # playerItemBase; 0 - current action available. 1 - current HP
    # playerItemsMax; 0 - current action max amount. 1 - max HP
    # On Rest; 0 - current Strength, 1 - current Magic, 2 -  current Skill, 3 - current HP
    # enemyItemsBase; 0 - name, 1 - current enemy HP, 2 - current enemy attacks
    # enemyItemsMax; 0 - name, 1 - max enemy HP, 2 - max enemy attacks

    def enemyAction(playerHP, enemyItemsBase, enemyItemsMax):
        # Check if enemy has the ability to attack
        if enemyItemsBase[2] > 0:
            for attack in reversed(range(0, enemyItemsBase[2] + 1)):

                # Check if number of attacks can do more than 90% damage on player
                if (attack * 6) >= (playerHP * 0.90) and attack > 1:
                    pass

                # If under 90% then enemy will attack or will attack if on last attack number
                else:
                    damageRolled = 0
                    for roll in range (0, attack):
                        damageRolled += random.randrange(1, 7)

                    # Roll for critical
                    if random.randrange(0, 20) == 19:
                        damageRolled  = int(damageRolled * 1.5)
                        print(' The enemy landed a critical hit!')
                        time.sleep(2)

                    break

            # Deal damage to the player
            playerHP -= damageRolled

            return playerHP, enemyItemsBase

        else:
            # Enemy recovers attack opportunities
            enemyItemsBase[2] += int(enemyItemsMax * 0.66)
            if enemyItemsBase[2] > enemyItemsMax[2]:
                enemyItemsBase[2] = enemyItemsMax[2]

            # Enemy recovers HP
            maxDifference = enemyItemsMax[1] - enemyItemsBase[1]
            healthRecover = int(enemyItemsMax[1] * 0.2)
            enemyItemsBase[1] += healthRecover
            if enemyItemsBase[1] > enemyItemsMax[1]:
                enemyItemsBase[1] = enemyItemsMax[1]
                print(f' {enemyItemsBase[0]} takes a rest recovering {maxDifference}')
            else:
                print(f' {enemyItemsBase[0]} takes a rest recovering {healthRecover}')

            return playerHP, enemyItemsBase

    if action == 'Strength':
        attackLineSetup = ' You have {} rolls available [{} damage].\n How many would you like to use? '
        damageRange = str(playerItemsBase[0] * 1) + ' - ' + str(playerItemsMax[0] * 6)
        playerChoice = input(attackLineSetup.format(playerItemsBase[0], damageRange))

        #try:
        common.clear()
        playerChoice = int(playerChoice)
        if playerChoice <= playerItemsBase[0]:
            damageRolled = 0
            if playerChoice > 1:
                for x in range(0, playerChoice):
                    damageRolled += random.randrange(1, 7)

            else:
                damageRolled += random.randrange(1, 7)

            while playerChoice >= 3:
                damageRolled = int(damageRolled * 1.5)
                playerChoice -= 3

            # Roll for critical!
            if random.randrange(0, 20) == 19:
                damageRolled = int(damageRolled * 1.5)
                print(' Landed a critical!')
                time.sleep(2)

            print(f" You hit {enemyItemsBase[0]} for {damageRolled}")
            enemyItemsBase[1] -= damageRolled
            time.sleep(1)

            # Check if enemy has HP
            if enemyItemsBase[1] > 0:
                workingList = enemyAction(playerItemsBase[1], enemyItemsBase, enemyItemsMax)

            else:
                pass



        else:
            print(f" You don't have enough {action} for that.")

        #except:
        #    print(' Invalid input.')
        #    time.sleep(2)

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

    return playerItemsBase, playerItemsMax, enemyItemsBase, enemyItemsMax

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

    enemyCurrent = [enemyName, enemyHPCurrent, enemyAttacksCurrent]
    enemyMax = [enemyName, enemyHPMax, enemyHPMax]
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
                    playerActionList = takeAction('Strength', playerStrength, playerStrengthLimit, enemyCurrent, enemyMax)
                    playerStrengthCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'm':
                if playerMagicCurrent < 1:
                    print(" You don't have enough magic left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Magic', playerMagic, playerMagicLimit, enemyCurrent, enemyMax)
                    playerMagicCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'k':
                if playerMagicCurrent < 1:
                    print(" You don't have enough skill left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Skill', playerSkill, playerSkillLimit, enemyCurrent, enemyMax)
                    playerMagicCurrent = playerActionList[0]
                    playerHPCurrent = playerActionList[1]

            elif playerAction == 'r':
                playerActionList = takeAction('Rest', playerRest, playerRestLimit, enemyCurrent, enemyMax)

            else:
                print(' Invalid action. Please try again.')
                time.sleep(2)


battleStart(playerBase, playerCurrent, enemyStats)