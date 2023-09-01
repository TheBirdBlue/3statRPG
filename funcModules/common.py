import os

#⦿ ○
#☐ ☒

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def numConversion(number):
    try:
        value = int(number)
        value = f'{value:,}'
        return value
    except (ValueError):
        return number

def hpbarCalculate(inputHP, inputHPMax):
    # Set up for the bar
    inputHP = int(inputHP)
    inputHPMax = int(inputHPMax)
    startingSize = 26
    percent = int(inputHP / inputHPMax)
    playerHPDisplay = ' ' + str(inputHP) + ' / ' + str(inputHPMax)

    # Check if input has more than 1 HP but percent calculates 0
    if inputHP > 0:
        percent = 1
    else:
        percent = 0

    # Calculate bar length
    barLength = startingSize - len(playerHPDisplay)
    percent = int((inputHP / inputHPMax) * barLength)

    # Begin the setup and return bar
    bar = '[' + ('▓' * percent) + ']'
    linePrint = ' ║ {:>' + str(barLength) + '} {:' + str(len(playerHPDisplay)) + '} ║'

    return linePrint.format(bar, playerHPDisplay)


def runUI(playerStats, playerCurrentHP, optionList):
    playerName = playerStats[0]
    playerHPMax = playerStats[1]
    playerStrength = playerStats[2]
    playerMagic = playerStats[3]
    playerSkill = playerStats[4]
    playerExp = playerStats[5]

    # UI set up
    topLine = '\n ╔══════════ {:^15} ════╗'
    playerHPLine = hpbarCalculate(playerCurrentHP, playerHPMax)
    breakLine = ' ╠═══════╦═══════╦═══════╦═══════╣'
    statLineOne = ' ║  STR  ║  MAG  ║  SKL  ║  EXP  ║'
    statLineTwo = ' ║ {:^5} ║ {:^5} ║ {:^5} ║ {:^5} ║'
    lineBreak = ' ╠═════╦═════════════════════════╣'
    optionsLine = ' ║{:^5}║ {:<24}║'
    bottomLine = ' ╚═════╩═════════════════════════╝\n'

    printOrder = [topLine.format(playerName), playerHPLine, breakLine, statLineOne,
                  statLineTwo.format(playerStrength, playerMagic, playerSkill, playerExp), lineBreak]

    # Print UI
    clear()
    for line in printOrder:
        print(line)
    optionNum = 1
    for option in optionList:
        print(optionsLine.format(str(optionNum), option))
        optionNum += 1
    print(bottomLine)
