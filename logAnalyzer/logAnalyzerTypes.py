from enum import Enum

# could store evaluation complexity / dependencies?
class CardValue:
  def __init__(self, value, messages=[]):
    self.value = value
    self.messages = messages