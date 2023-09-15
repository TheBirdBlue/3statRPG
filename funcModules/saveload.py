import os

def createPlayer(name):
    loadOrder = ['', 10, 3, 3, 3, 0]
    fileLocation = './saves/' + name
    os.makedirs(fileLocation)
    loadOrder[0] = name
    file = './saves/' + name + '/playerSave.txt'
    with open(file, 'a+') as save:
        for spot in loadOrder:
            save.write(str(spot) + '\n')

    return loadOrder

def loadPlayer(name):
    loadOrder = []
    fileLocation = './saves/' + name + '/playerSave.txt'
    with open(fileLocation, 'r') as save:
        for line in save:
            try:
                line = line.replace('\n', '')
                line = int(line)
                loadOrder.append(line)
            except:
                line = line.replace('\n', '')
                loadOrder.append(line)

    return loadOrder

def savePlayer(charStats):
    saveOrder = []
    for stat in charStats:
        saveOrder.append(stat)

    fileLocation = './saves/' + charStats[0] + '/playerSave.txt'

    with open(fileLocation, 'w') as save:
        for line in saveOrder:
            str(line).rstrip('\n')
            save.write(str(line) + '\n')
