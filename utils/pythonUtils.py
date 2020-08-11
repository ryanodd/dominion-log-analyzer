def getObjectMembers(object):
  members = [attr for attr in dir(object) if not callable(getattr(object, attr)) and not attr.startswith("__")]
  return members 