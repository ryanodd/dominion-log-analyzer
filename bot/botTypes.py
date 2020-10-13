from enum import Enum

# could store evaluation complexity / dependencies?
class botValue:
  def __init__(self, value, evaluator=None, message='', importance=100):
    self.value = value

    self.evaluator = evaluator # function to evaluate with
    self.evaluationNeeded = self.evaluator is not None # stateful flag
    self.message = message

    self.importance = importance # how necessary is evaluation for the value's usefulness?