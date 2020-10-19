from game.card.gCardFactory import getCard


# Unlike CardFactory's getCard, this works on pluralized versions of card names
def getCardByName(testString):
  if testString in nameToCard:
    return nameToCard[testString]
  elif testString in namePluralToCard:
    return namePluralToCard[testString]
  return None

nameToCard = {}
namePluralToCard = {}



nameToCard['Copper'] = getCard('Copper')
namePluralToCard['Coppers'] = getCard('Copper')

nameToCard['Curse'] = getCard('Curse')
namePluralToCard['Curses'] = getCard('Curse')

nameToCard['Estate'] = getCard('Estate')
namePluralToCard['Estates'] = getCard('Estate')

nameToCard['Silver'] = getCard('Silver')
namePluralToCard['Silvers'] = getCard('Silver')

nameToCard['Duchy'] = getCard('Duchy')
namePluralToCard['Duchies'] = getCard('Duchy')

nameToCard['Gold'] = getCard('Gold')
namePluralToCard['Golds'] = getCard('Gold')

nameToCard['Province'] = getCard('Province')
namePluralToCard['Provinces'] = getCard('Province')



nameToCard['Cellar'] = getCard('Cellar')
namePluralToCard['Cellars'] = getCard('Cellar')

nameToCard['Chapel'] = getCard('Chapel')
namePluralToCard['Chapels'] = getCard('Chapel')

nameToCard['Moat'] = getCard('Moat')
namePluralToCard['Moats'] = getCard('Moat')

nameToCard['Harbinger'] = getCard('Harbinger')
namePluralToCard['Harbingers'] = getCard('Harbinger')

nameToCard['Merchant'] = getCard('Merchant')
namePluralToCard['Merchants'] = getCard('Merchant')

nameToCard['Vassal'] = getCard('Vassal')
namePluralToCard['Vassals'] = getCard('Vassal')

nameToCard['Village'] = getCard('Village')
namePluralToCard['Villages'] = getCard('Village')

nameToCard['Workshop'] = getCard('Workshop')
namePluralToCard['Workshops'] = getCard('Workshop')

nameToCard['Bureaucrat'] = getCard('Bureaucrat')
namePluralToCard['Bureaucrats'] = getCard('Bureaucrat')

nameToCard['Gardens'] = getCard('Gardens')
namePluralToCard['Gardens'] = getCard('Gardens')

nameToCard['Militia'] = getCard('Militia')
namePluralToCard['Militias'] = getCard('Militia')

nameToCard['Moneylender'] = getCard('Moneylender')
namePluralToCard['Moneylenders'] = getCard('Moneylender')

nameToCard['Poacher'] = getCard('Poacher')
namePluralToCard['Poachers'] = getCard('Poacher')

nameToCard['Remodel'] = getCard('Remodel')
namePluralToCard['Remodels'] = getCard('Remodel')

nameToCard['Smithy'] = getCard('Smithy')
namePluralToCard['Smithies'] = getCard('Smithy')

nameToCard['Throne Room'] = getCard('Throne Room')
namePluralToCard['Throne Rooms'] = getCard('Throne Room')

nameToCard['Bandit'] = getCard('Bandit')
namePluralToCard['Bandits'] = getCard('Bandit')

nameToCard['Council Room'] = getCard('Council Room')
namePluralToCard['Council Rooms'] = getCard('Council Room')

nameToCard['Festival'] = getCard('Festival')
namePluralToCard['Festivals'] = getCard('Festival')

nameToCard['Laboratory'] = getCard('Laboratory')
namePluralToCard['Laboratories'] = getCard('Laboratory')

nameToCard['Library'] = getCard('Library')
namePluralToCard['Libraries'] = getCard('Library')

nameToCard['Market'] = getCard('Market')
namePluralToCard['Markets'] = getCard('Market')

nameToCard['Mine'] = getCard('Mine')
namePluralToCard['Mines'] = getCard('Mine')

nameToCard['Sentry'] = getCard('Sentry')
namePluralToCard['Sentries'] = getCard('Sentry')

nameToCard['Witch'] = getCard('Witch')
namePluralToCard['Witches'] = getCard('Witch')

nameToCard['Artisan'] = getCard('Artisan')
namePluralToCard['Artisans'] = getCard('Artisan')
