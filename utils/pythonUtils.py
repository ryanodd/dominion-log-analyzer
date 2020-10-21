def getObjectMembers(object):
  members = [attr for attr in dir(object) if not callable(getattr(object, attr)) and not attr.startswith("__")]
  return members 

def removeItemsFromList(originalList, itemsToRemove):
  newList = []
  for e in originalList:
    if e not in itemsToRemove:
      newList.append(e)
    originalList = newList