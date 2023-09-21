import time
import random
import common

def levelStat(hp, stat, experience, skillName):
    # For increasing HP only
    if skillName == 'HP':
        cost = int(hp/3) + 1
        lineFormat = f"\n It will cost {cost} experience to increase {skillName} by 3. Continue (Y or N)?  "
        playerConfirmation = input(lineFormat)
        playerConfirmation = playerConfirmation.lower()
        if playerConfirmation == 'y':
            # Check that experience is enough to upgrade stat
            if experience >= cost:
                hp += 3
                experience -= cost
                return hp, experience

    # For all over stats
    else:
        cost = stat + 1
        lineFormat = f"\n It will cost {cost} experience to level up {skillName} by 1. Continue (Y or N)?  "
        playerConfirmation = input(lineFormat)
        playerConfirmation = playerConfirmation.lower()
        if playerConfirmation == 'y':
            # Check that experience is enough to upgrade stat
            if experience >= cost:
                stat += 1
                hp += 1
                experience -= cost
                return hp, stat, experience
            else:
                print(' Not enough experience.')
                time.sleep(2)
                return hp, stat, experience
        else:
            print(' Confirmation not received.')
            return hp, stat, experience

def levelUp(playerStats):
    training = True
    playerName = playerStats[0]
    playerHP = playerStats[1]
    playerStrength = playerStats[2]
    playerMagic = playerStats[3]
    playerSkill = playerStats[4]
    playerExp = playerStats[5]

    trainingOptions = ['Train Health', 'Train Strength', 'Train Magic', 'Train Skill', 'Return']

    hintOne = " Using 3 or more Strength in battle will give a 1.5x damage bonus."
    hintTwo = " Using 3 or more Magic in battle will inflict Magic Sap and do chip damage."
    hintThree = " Using 3 or more Skill in battle may make your enemy miss on their turn."
    hintFour = " Strength is the only stat that has a chance of a critical hit."
    hintFive = " Exiting a dungeon yields bonus Exp while retreating does not."
    hintSix = " This is a placeholder. You had a 1 in 10 chance of getting it."
    randomOne = " Did you get time outside today?"
    randomTwo = " Be sure to call your mom!"
    randomThree = " This is the 6th project in the Python CLI series I've created."
    randomFour = " Shoutout to SimpleFlips."

    messageList = [hintOne, hintTwo, hintThree, hintFour, hintFive, hintSix, randomOne, randomTwo, randomThree,
                   randomFour]

    while training:
        print(messageList[random.randrange(0, len(messageList))])
        common.runUI(playerStats, playerHP, trainingOptions)

        playerInput = input(' Please pick an option to train:  ')

        try:
            playerInput = int(playerInput)

            if playerInput == 1:
                playerHPList = levelStat(playerHP, playerHP, playerExp, 'HP')
                playerHP = playerHPList[0]
                playerExp = playerHPList[1]

            elif playerInput == 2:
                playerStrengthList = levelStat(playerHP, playerStrength, playerExp, 'strength')
                playerHP = playerStrengthList[0]
                playerStrength = playerStrengthList[1]
                playerExp = playerStrengthList[2]

            elif playerInput == 3:
                playerMagicList = levelStat(playerHP, playerMagic, playerExp, 'magic')
                playerHP = playerMagicList[0]
                playerMagic = playerMagicList[1]
                playerExp = playerMagicList[2]

            elif playerInput == 4:
                playerSkillList = levelStat(playerHP, playerSkill, playerExp, 'skill')
                playerHP = playerSkillList[0]
                playerSkill = playerSkillList[1]
                playerExp = playerSkillList[2]

            elif playerInput == 5:
                training = False
                return playerStats

            playerStats = [playerName, playerHP, playerStrength, playerMagic, playerSkill, playerExp]

        except:
            print(' Invalid input')
            time.sleep(2)
