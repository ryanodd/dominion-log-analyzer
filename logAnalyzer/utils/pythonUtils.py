def getObjectMembers(object):
    members = [attr for attr in dir(object) if not callable(
        getattr(object, attr)) and not attr.startswith("__")]
    return members

# once per occurrence in itemsToRemove


def removeItemsFromList(listReference, itemsToRemove):
    for e in itemsToRemove:
        if e in listReference:
            listReference.remove(e)
