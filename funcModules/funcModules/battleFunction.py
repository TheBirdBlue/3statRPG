import random
import time
import common
import math

# # # FOR TESTING PURPOSES / INACTIVE # # #
'''playerStats = ['TEST', 10, 3, 3, 3, 0]
enemyStats = ['Slime Rat', 10, 2]

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
playerCurrent = [playerHPCurrent, playerStrengthCurrent, playerMagicCurrent, playerSkillCurrent, playerExp]

enemyName = enemyStats[0]
enemyHPMax = enemyStats[1]
enemyAttacksMax = enemyStats[2]
enemyHPCurrent = enemyHPMax
enemyAttacksCurrent = enemyAttacksMax'''
# # # END TESTING DATA / INACTIVE # # #

unused = '⦿'
used = '○'
magcount = 0

def readout(base):
    attackLineSetup = ' You have {} rolls available [{} damage].\n How many would you like to use?  '
    damageRange = str(base * 1) + ' - ' + str(base * 6)
    playerChoice = input(attackLineSetup.format(base, damageRange))
    return playerChoice

def drawUI(playerBase, playerCurrent, enemyBase, enemyCurrent):
    # Set up common name variables for player
    playerHPMax = playerBase[0]
    playerStrengthMax = playerBase[1]
    playerMagicMax = playerBase[2]
    playerSkillMax = playerBase[3]
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
    if enemyName.lower() == 'none':
        pass
    else:
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

def generateEnemy(rank):
    standard = ['name', 10, 2]
    namePrefix = ['Slimed', 'Non-Elemental', 'Hellish', 'Glorified', 'Mini', 'Garden Variety', 'Royale']
    nameFocus = ['Rat', 'Slime', 'Wolf', 'Spider', 'Thief', 'Mage', 'Bandit', 'Vines', 'Skunk', 'Marksman']

    # Generate Name
    namePrefixSelected = namePrefix[random.randrange(0, len(namePrefix))]
    nameFocusSelected = nameFocus[random.randrange(0, len(nameFocus))]
    standard[0] = namePrefixSelected + ' ' + nameFocusSelected

    # Adjust HP for rank
    if rank > 1:
        standard[1] = standard[1] + int(standard[1] * (rank / 10))
    else:
        pass

    # Adjust attacks for rank
    if rank > 1:
        standard[2] = int(standard[2] + math.ceil(rank/3))
    else:
        pass

    return standard


def takeAction(action, playerItemsBase, playerItemsMax, enemyItemsBase, enemyItemsMax):

    # playerItemBase; 0 - current action available. 1 - current HP
    # playerItemsMax; 0 - current action max amount. 1 - max HP
    # On Rest; 0 - current Strength, 1 - current Magic, 2 -  current Skill, 3 - current HP
    # enemyItemsBase; 0 - name, 1 - current enemy HP, 2 - current enemy attacks
    # enemyItemsMax; 0 - name, 1 - max enemy HP, 2 - max enemy attacks

    global magcount
    attacked = False

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
            print(f" {enemyItemsBase[0]} hit for {damageRolled}.")
            time.sleep(2)

            return playerHP, enemyItemsBase

        # Enemy has no attacks to initiates the rest action
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

    # Strength process which focuses on extra damage
    if action == 'Strength':
        playerChoice = readout(playerItemsBase[0])

        #try:
        common.clear()
        playerChoice = int(playerChoice)
        if playerChoice <= playerItemsBase[0]:
            playerItemsBase[0] -= playerChoice
            damageRolled = 0
            if playerChoice > 1:
                for x in range(0, playerChoice):
                    damageRolled += random.randrange(1, 7)

            else:
                damageRolled += random.randrange(1, 7)

            # Strength special; added damage per 3 used
            while playerChoice >= 3:
                damageRolled = int(damageRolled * 1.5)
                playerChoice -= 3

            # Roll for critical!
            if random.randrange(0, 20) == 19:
                damageRolled = int(damageRolled * 1.5)
                print(' Landed a critical!')
                time.sleep(2)

            print(f" You hit {enemyItemsBase[0]} for {damageRolled}")
            attacked = True
            enemyItemsBase[1] -= damageRolled
            time.sleep(1)

            # Check if enemy has HP
            if enemyItemsBase[1] > 0:
                workingList = enemyAction(playerItemsBase[1], enemyItemsBase, enemyItemsMax)
                playerItemsBase[1] = workingList[0]
                enemyItemsBase = workingList[1]

            else:
                pass

        else:
            print(f" You don't have enough {action} for that.")
            time.sleep(2)

        #except:
        #    print(' Invalid input.')
        #    time.sleep(2)

    # Magic process which focuses on sapping damage
    elif action == 'Magic':
        playerChoice = readout(playerItemsBase[0])

        #try
        common.clear()
        playerChoice = int(playerChoice)
        if playerChoice <= playerItemsBase[0]:
            playerItemsBase[0] -= playerChoice
            damageRolled = 0
            if playerChoice > 1:
                for x in range(0, playerChoice):
                    damageRolled += random.randrange(1, 7)

            else:
                damageRolled += random.randrange(1, 7)

            # Magic special; inflict magic sap
            if playerChoice >= 3:
                magcount = 3
                print(f'\n {enemyName} has been afflicted with magic sap.')
                time.sleep(2)

            print(f" You hit {enemyItemsBase[0]} for {damageRolled}")
            attacked = True
            enemyItemsBase[1] -= damageRolled
            time.sleep(1)

            # Check if enemy has HP
            if enemyItemsBase[1] > 0:
                workingList = enemyAction(playerItemsBase[1], enemyItemsBase, enemyItemsMax)
                playerItemsBase[1] = workingList[0]
                enemyItemsBase = workingList[1]

            else:
                pass

        else:
            print(f" You don't have enough {action} for that.")
            time.sleep(2)

        #except:
        #    print(' Invalid input.')
        #    time.sleep(2)

    elif action == 'Skill':
        playerChoice = readout(playerItemsBase[0])

        #try
        common.clear()
        playerChoice = int(playerChoice)
        if playerChoice <= playerItemsBase[0]:
            playerItemsBase[0] -= playerChoice
            damageRolled = 0
            if playerChoice > 1:
                for x in range(0, playerChoice):
                    damageRolled += random.randrange(1, 7)

            else:
                damageRolled += random.randrange(1, 7)

            print(f" You hit {enemyItemsBase[0]} for {damageRolled}")
            attacked = False
            enemyItemsBase[1] -= damageRolled
            time.sleep(1)

            if enemyItemsBase[1] > 0:
                if playerChoice >= 3:
                    dodgeRoll = random.randrange(0, 100)
                else:
                    dodgeRoll = 1

                if dodgeRoll >= 50:
                    if enemyItemsBase[1] > 0:
                        print(' Dodged the enemy attack!')
                        time.sleep(2)

                else:
                    workingList = enemyAction(playerItemsBase[1], enemyItemsBase, enemyItemsMax)
                    playerItemsBase[1] = workingList[0]
                    enemyItemsBase = workingList[1]

        else:
            print(f" You don't have enough {action} for that.")
            time.sleep(2)

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
        attacked = True
        print(recoveryLine.format(recoveryRead[0], recoveryRead[1], recoveryRead[2], recoveryRead[3]))
        time.sleep(2)

        workingList = enemyAction(playerItemsBase[1], enemyItemsBase, enemyItemsMax)
        playerItemsBase[1] = workingList[0]
        enemyItemsBase = workingList[1]

    # Do magic sap damage if applied
    if attacked:
        if magcount > 0 and enemyItemsBase[1] > 0:
            magDamage = int(enemyItemsBase[1] * 0.1)

            if magDamage < 1:
                magDamage = 1

            enemyItemsBase[1] -= magDamage
            print(f"\n Your magic sapped {magDamage} from {enemyName}.")
            time.sleep(2)

    return playerItemsBase, playerItemsMax, enemyItemsBase, enemyItemsMax

def battleStart(playerBase, playerCurrent, rank):

    # Set up common name variables for player
    playerHPMax = playerBase[0]
    playerStrengthMax = playerBase[1]
    playerMagicMax = playerBase[2]
    playerSkillMax = playerBase[3]
    playerHPCurrent = playerCurrent[0]
    playerStrengthCurrent = playerCurrent[1]
    playerMagicCurrent = playerCurrent[2]
    playerSkillCurrent = playerCurrent[3]

    # Generate monster and set up common name variables for enemy
    enemyStats = generateEnemy(rank)
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
        drawUI(playerBase, playerCurrent, enemyMax, enemyCurrent)

        # Check is player can take an action. If unable, forces rest action for the turn
        if playerStrengthCurrent and playerMagicCurrent and playerSkillCurrent < 1:
            print(" You have to take a rest action.")
            time.sleep(2)
            playerActionList = takeAction(playerRest, enemyCurrent)

        # If player can take action, allows player to choose and fight
        else:

            print('\n What action will you roll?')
            playerAction = input(' (S)TR | (M)AG | S(K)L | (R)est\n Action:  ')
            playerAction = playerAction.lower()

            if playerAction == 's':
                if playerStrengthCurrent < 1:
                    print(" You don't have enough strength left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Strength', playerStrength, playerStrengthLimit, enemyCurrent,
                                                  enemyMax)
                    playerStrengthCurrent = playerActionList[0][0]
                    playerHPCurrent = playerActionList[0][1]
                    enemyHPCurrent = playerActionList[2][1]
                    enemyAttacksCurrent = playerActionList[2][2]

            elif playerAction == 'm':
                if playerMagicCurrent < 1:
                    print(" You don't have enough magic left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Magic', playerMagic, playerMagicLimit, enemyCurrent, enemyMax)
                    playerMagicCurrent = playerActionList[0][0]
                    playerHPCurrent = playerActionList[0][1]
                    enemyHPCurrent = playerActionList[2][1]
                    enemyAttacksCurrent = playerActionList[2][2]

            elif playerAction == 'k':
                if playerMagicCurrent < 1:
                    print(" You don't have enough skill left")
                    time.sleep(2)
                else:
                    playerActionList = takeAction('Skill', playerSkill, playerSkillLimit, enemyCurrent, enemyMax)
                    playerSkillCurrent = playerActionList[0][0]
                    playerHPCurrent = playerActionList[0][1]
                    enemyHPCurrent = playerActionList[2][1]
                    enemyAttacksCurrent = playerActionList[2][2]

            elif playerAction == 'r':
                playerActionList = takeAction('Rest', playerRest, playerRestLimit, enemyCurrent, enemyMax)

            else:
                print(' Invalid action. Please try again.')
                time.sleep(2)

        playerCurrent[0] = playerHPCurrent
        playerCurrent[1] = playerStrengthCurrent
        playerCurrent[2] = playerMagicCurrent
        playerCurrent[3] = playerSkillCurrent

        # For when enemy id defeated
        if enemyHPCurrent <= 0 and playerHPCurrent >= 1:
            battlestate = False
            print('\n And there goes the battle! To the victor, the spoils.')
            playerCurrent[4] += rank
            time.sleep(2)

        # For when player is defeated
        elif playerHPCurrent <= 0:
            battlestate = False

    print(playerCurrent)
    return playerCurrent
