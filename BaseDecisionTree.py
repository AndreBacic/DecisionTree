
class BaseDecisionTree(object):
    """
    A decision tree that classifies objects of type supportedDataType
    """
    def __init__(self, root: 'Branch', supportedDataType: type) -> None:
        self.root = root
        self.supportedDataType = supportedDataType
    
    def classify(self, obj):
        if not isinstance(obj, self.supportedDataType): return None

        return self.root.classify(obj)

class Branch():
    """
    Given a decisionFunc that takes an object and returns a bool, 
    a Branch will choose its left node (self.l) if the function returns true, 
    and its right node (self.r) otherwise.

    Valid types for self.l and self.r are Branch or Leaf.
    """
    def __init__(self, decisionFunc: function) -> None:
        self.l: 'Branch' or 'Leaf' = None
        self.r: 'Branch' or 'Leaf' = None
        self.decisionFunc = decisionFunc

    def classify(self, obj) -> str:
        if self.decisionFunc(obj):
            return self.l.classify(obj)
        return self.r.classify(obj)

class Leaf():
    """
    A final decision node of a decision tree that holds a string value that is the classification.
    """
    def __init__(self, value: str) -> None:
        self.value = value

    def classify(self, obj) -> str:
        return self.value
