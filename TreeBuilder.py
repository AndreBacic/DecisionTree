
# TODO: Create a class to make a decision tree based on a data set 
# and then save it to a new .py file as a class extending BaseDecisionTree


from typing import List
import math

class DecisionTreeBuilder:
    def __init__(self, max_depth: int = 9999, min_node_size: int = 1) -> None:
        self.max_depth = abs(max_depth)
        self.min_node_size = abs(min_node_size) # TODO: finish this class

    def calculateMaxInfoGain(self, labels: List[str], properties: List) -> float:
        if not (properties and labels) or len(properties) != len(labels): return 0

        max_info_gain = 0
        H = self.calculateGiniImpurity(labels)
        l = len(labels)
        l1 = []
        l2 = list(labels)
        for i in properties:
            l1.append(l2.pop(0))

            H1 = self.calculateGiniImpurity(l1) * len(l1) / l
            H2 = self.calculateGiniImpurity(l2) * len(l2) / l
            gain = H - H1 - H2
            if gain > max_info_gain:
                max_info_gain = gain
        
        return max_info_gain


    def calculateGiniImpurity(self, input: List) -> float:
        # return 1 - Sum from i=1 to n of (Probability(Xi)**2)
        if not input: return 0.0

        probs = dict()
        p = 1 / len(input)
        for i in input:
            if probs.get(i):
                probs[i] += p
                continue
            probs[i] = p
        
        s = 1.0
        for i in probs.values():
            s -= i*i # retrns the negative of the sum, so just minus each time.
        
        s = round(s, 7) # resolves some weird rounding errors
        return s