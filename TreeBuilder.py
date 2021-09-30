from BaseDecisionTree import *
from typing import Dict, List, Tuple
import uuid
from TreeWriter import DecisionTreeWriter

class DecisionTreeBuilder(DecisionTreeWriter): # TODO: make internal methods private
    """
    Makes a decision tree based on a data set
    """
    def __init__(self, max_depth: int = 9999, min_node_size: int = 1, label_name = "LABEL") -> None:
        super().__init__(max_depth, min_node_size, label_name)


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
            properties = list(map(lambda x: x[field], data_set))
            labels = list(map(lambda x: x[self.label_name], data_set))
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

    