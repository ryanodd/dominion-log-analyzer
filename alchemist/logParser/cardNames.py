from game.card.gCardFactory import getGCard


# Unlike CardFactory's getCard, this works on pluralized versions of card names
def getCardByName(testString):
  if testString in nameToCard:
    return nameToCard[testString]
  elif testString in namePluralToCard:
    return namePluralToCard[testString]
  return None

nameToCard = {}
namePluralToCard = {}



nameToCard['Copper'] = getGCard('Copper')
namePluralToCard['Coppers'] = getGCard('Copper')

nameToCard['Curse'] = getGCard('Curse')
namePluralToCard['Curses'] = getGCard('Curse')

nameToCard['Estate'] = getGCard('Estate')
namePluralToCard['Estates'] = getGCard('Estate')

nameToCard['Silver'] = getGCard('Silver')
namePluralToCard['Silvers'] = getGCard('Silver')

nameToCard['Duchy'] = getGCard('Duchy')
namePluralToCard['Duchies'] = getGCard('Duchy')

nameToCard['Gold'] = getGCard('Gold')
namePluralToCard['Golds'] = getGCard('Gold')

nameToCard['Province'] = getGCard('Province')
namePluralToCard['Provinces'] = getGCard('Province')



nameToCard['Cellar'] = getGCard('Cellar')
namePluralToCard['Cellars'] = getGCard('Cellar')

nameToCard['Chapel'] = getGCard('Chapel')
namePluralToCard['Chapels'] = getGCard('Chapel')

nameToCard['Moat'] = getGCard('Moat')
namePluralToCard['Moats'] = getGCard('Moat')

nameToCard['Harbinger'] = getGCard('Harbinger')
namePluralToCard['Harbingers'] = getGCard('Harbinger')

nameToCard['Merchant'] = getGCard('Merchant')
namePluralToCard['Merchants'] = getGCard('Merchant')

nameToCard['Vassal'] = getGCard('Vassal')
namePluralToCard['Vassals'] = getGCard('Vassal')

nameToCard['Village'] = getGCard('Village')
namePluralToCard['Villages'] = getGCard('Village')

nameToCard['Workshop'] = getGCard('Workshop')
namePluralToCard['Workshops'] = getGCard('Workshop')

nameToCard['Bureaucrat'] = getGCard('Bureaucrat')
namePluralToCard['Bureaucrats'] = getGCard('Bureaucrat')

nameToCard['Gardens'] = getGCard('Gardens')
namePluralToCard['Gardens'] = getGCard('Gardens')

nameToCard['Militia'] = getGCard('Militia')
namePluralToCard['Militias'] = getGCard('Militia')

nameToCard['Moneylender'] = getGCard('Moneylender')
namePluralToCard['Moneylenders'] = getGCard('Moneylender')

nameToCard['Poacher'] = getGCard('Poacher')
namePluralToCard['Poachers'] = getGCard('Poacher')

nameToCard['Remodel'] = getGCard('Remodel')
namePluralToCard['Remodels'] = getGCard('Remodel')

nameToCard['Smithy'] = getGCard('Smithy')
namePluralToCard['Smithies'] = getGCard('Smithy')

nameToCard['Throne Room'] = getGCard('Throne Room')
namePluralToCard['Throne Rooms'] = getGCard('Throne Room')

nameToCard['Bandit'] = getGCard('Bandit')
namePluralToCard['Bandits'] = getGCard('Bandit')

nameToCard['Council Room'] = getGCard('Council Room')
namePluralToCard['Council Rooms'] = getGCard('Council Room')

nameToCard['Festival'] = getGCard('Festival')
namePluralToCard['Festivals'] = getGCard('Festival')

nameToCard['Laboratory'] = getGCard('Laboratory')
namePluralToCard['Laboratories'] = getGCard('Laboratory')

nameToCard['Library'] = getGCard('Library')
namePluralToCard['Libraries'] = getGCard('Library')

nameToCard['Market'] = getGCard('Market')
namePluralToCard['Markets'] = getGCard('Market')

nameToCard['Mine'] = getGCard('Mine')
namePluralToCard['Mines'] = getGCard('Mine')

nameToCard['Sentry'] = getGCard('Sentry')
namePluralToCard['Sentries'] = getGCard('Sentry')

nameToCard['Witch'] = getGCard('Witch')
namePluralToCard['Witches'] = getGCard('Witch')

nameToCard['Artisan'] = getGCard('Artisan')
namePluralToCard['Artisans'] = getGCard('Artisan')
