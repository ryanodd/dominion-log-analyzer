from enum import Enum

class AlgorithmComplexity(Enum):
  ONE = 1
  LOGN = 2
  N = 3
  NLOGN = 4
  NSQUARED = 5

class botValue:
  def __init__(self, value, evaluator=None , importance=100, complexity=AlgorithmComplexity.ONE):
    self.value = value

    self.evaluator = evaluator # function to evaluate with
    self.evaluationNeeded = self.evaluator is not None # stateful flag

    self.complexity = complexity # Evaluator function algorithm complexity
    self.importance = importance # how necessary is evaluation for the value's usefulness?