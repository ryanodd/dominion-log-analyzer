from utils.log import logError

# Maps card names to CardInfo objects
value = {}

def estate():
    return 0
value['Estate'] = estate

def duchy():
    return 0
value['Duchy'] = duchy

def province():
    return 0
value['Province'] = province

def curse():
    return 0
value['Curse'] = curse

def copper():
    return 1
value['Copper'] = copper

def silver():
    return 2
value['Silver'] = silver

def gold():
    return 3
value['Gold'] = gold

def getCardValue(name):
    if name not in value:
        logError('name \'%s\' not found' % name)
    return value[name]
