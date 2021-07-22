boons = {}

boons['The Earth\'s Gift'] = 'The Earth\'s Gift'
boons['The Field\'s Gift'] = 'The Field\'s Gift'
boons['The Flame\'s Gift'] = 'The Flame\'s Gift'
boons['The Forest\'s Gift'] = 'The Forest\'s Gift'
boons['The Moon\'s Gift'] = 'The Moon\'s Gift'
boons['The Mountain\'s Gift'] = 'The Mountain\'s Gift'
boons['The River\'s Gift'] = 'The River\'s Gift'
boons['The Sea\'s Gift'] = 'The Sea\'s Gift'
boons['The Sky\'s Gift'] = 'The Sky\'s Gift'
boons['The Sun\'s Gift'] = 'The Sun\'s Gift'
boons['The Swamp\'s Gift'] = 'The Swamp\'s Gift'
boons['The Wind\'s Gift'] = 'The Wind\'s Gift'

hexes = {}

hexes['Bad Omens'] = 'Bad Omens'
hexes['Delusion'] = 'Delusion'
hexes['Envy'] = 'Envy'
hexes['Famine'] = 'Famine'
hexes['Fear'] = 'Fear'
hexes['Greed'] = 'Greed'
hexes['Haunting'] = 'Haunting'
hexes['Locusts'] = 'Locusts'
hexes['Misery'] = 'Misery'
hexes['Plague'] = 'Plague'
hexes['Poverty'] = 'Poverty'
hexes['War'] = 'War'

states = {}

states['Lost in the Woods'] = 'Lost in the Woods'
states['Deluded'] = 'Deluded'
states['Envious'] = 'Envious'
states['Miserable'] = 'Miserable'
states['Twice Miserable'] = 'Twice Miserable'


def getBoonOrHexOrState(name):
    if name in boons:
        return boons[name]
    if name in hexes:
        return hexes[name]
    if name in states:
        return states[name]
    return None
