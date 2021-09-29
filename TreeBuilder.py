from BaseDecisionTree import *
from typing import Dict, List, Tuple
import uuid

class DecisionTreeBuilder:
    """
    Makes a decision tree based on a data set 
    and then saves it to a new .py file as a class extending BaseDecisionTree
    """
    def __init__(self, max_depth: int = 9999, min_node_size: int = 1, label_name = "LABEL") -> None:
        self.max_depth = abs(max_depth)
        self.min_node_size = abs(min_node_size)
        self.label_name = label_name

    def build_tree(self, data_set: List[Dict], tree_name: str = "DecisionTreeModel") -> 'BaseDecisionTree':
        tree = BaseDecisionTree(None, dict, f"{tree_name}{uuid.uuid4()}")
        # TODO: 1) Add fields (key-value pairs) for combined basic fields
        # Not yet implemented
        expandedDataSet = list(data_set)
        # 2) recursively build branches or leaves based on best fit
        tree.root = self.build_branch(expandedDataSet, 1)

        return tree

    def build_branch(self, data_set: List[Dict], depth: int) -> 'Branch' or 'Leaf':
        # 1) check that all labels are different
        labels_are_same, primary_label = self.check_labels(data_set)
        if labels_are_same or depth >= self.max_depth or len(data_set) < self.min_node_size:
            return Leaf(primary_label)

        # 2) Find best field to split on and what value of it to split by        
        max_gain = 0
        for field in data_set[0].keys():
            if field == self.label_name:
                continue
            data_set.sort(key = lambda x: x.get(field))
            properties = map(lambda x: x[field], data_set)
            labels = map(lambda x: x[self.label_name], data_set)
            gain, split_point = self.calculate_max_gini_gain(labels, properties)
            if gain > max_gain:
                max_gain = gain
                value_to_split_by = split_point
                field_to_split_by = field

        # 3) Perform the decision split
        left_data_set, right_data_set = self.split_data(data_set, field_to_split_by, value_to_split_by)

        # 4) Create new Branch
        new_branch = Branch(lambda x: x[field_to_split_by] <= value_to_split_by)

        # 5) Recursively build new branches
        depth+=1
        new_branch.l = self.build_branch(left_data_set, depth)
        new_branch.r = self.build_branch(right_data_set, depth)

        return new_branch

    def check_labels(self, data_set: List[Dict]) -> Tuple[bool, str]:
        counted_labels = dict()
        primary_label = None
        primary_label_count = 0
        for i in data_set:
            if counted_labels.get(i[self.label_name]):
                counted_labels[i[self.label_name]] += 1
            else:
                counted_labels[i[self.label_name]] = 1
            
            if counted_labels[i[self.label_name]] > primary_label_count:
                primary_label_count = counted_labels[i[self.label_name]]
                primary_label = i[self.label_name]
        
        if len(counted_labels.keys()) == 1:
            return True, primary_label

        return False, primary_label

        

    def split_data(self, data_set: List[Dict], field_to_split_by: str, value_to_split_by) -> Tuple[List[Dict], List[Dict]]:
        left = []
        right = []
        for item in data_set:
            if item[field_to_split_by] <= value_to_split_by:
                left.append(item)
            else:
                right.append(item)

        return left, right

    def create_tree_file(self, tree: 'BaseDecisionTree') -> None:
        # TODO: Scoffold out code in a new file for this new tree
        file = open()

    def calculate_max_gini_gain(self, labels: List[str], properties: List) -> Tuple[float, float]:
        if not (properties and labels) or len(properties) != len(labels): return 0

        max_gain = 0
        H = self.calculate_gini_impurity(labels)
        l = len(labels)
        l1 = []
        l2 = list(labels)
        value_to_split_by = None
        for i, val in enumerate(properties):
            l1.append(l2.pop(0))
            if len(l2) == 0: break

            H1 = self.calculate_gini_impurity(l1) * len(l1) / l
            H2 = self.calculate_gini_impurity(l2) * len(l2) / l
            gain = H - H1 - H2
            if gain > max_gain:
                max_gain = gain
                value_to_split_by = (val + properties[i+1])/2
        
        return max_gain, value_to_split_by


    def calculate_gini_impurity(self, input: List) -> float:
        """
        Returns the Gini impurity of input (0 means all of the items are the same, > 0.5 is pretty mixed)
        """
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