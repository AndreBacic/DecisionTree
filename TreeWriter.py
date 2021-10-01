from BaseDecisionTree import *
from typing import Dict, List, Tuple
import uuid, math

class DecisionTreeWriter:
    """
    Makes a decision tree based on a data set 
    and then saves it to a new .py file as a class extending BaseDecisionTree
    """
    def __init__(self, max_depth: int = 998, min_node_size: int = 1, label_name = "LABEL") -> None:
        self.max_depth = abs(max_depth)
        self.min_node_size = abs(min_node_size)
        self.label_name = label_name

        self.supported_field_types = [int, float, bool]

        self.__field_access_prefix = "."
        self.__field_access_postfix = ""


    def build_tree(self, data_set: List[Dict or object], look_for_correlations: bool = True, tree_name: str = "DecisionTreeModel") -> None:
        guid = str(uuid.uuid4()).replace('-', '_')
        file_name = f"{tree_name}__{guid}"
        file = ["from BaseDecisionTree import *",
                "",
                "# class-like syntax because it acts like it's instantiating a class.",
               f"def {file_name}() -> 'BaseDecisionTree':",
                '    """',
               f"    {file_name} has been trained to identify the {self.label_name} of a given dictionary object.",
                '    """',
               f"    tree = BaseDecisionTree(None, dict, '{file_name}')"]

        # 1) Format data_set
        expanded_data_set = []

        if type(data_set[0]) != dict:
            expanded_data_set = list(map(lambda x: x.__dict__, data_set))
            self.__field_access_prefix = "."
            self.__field_access_postfix = ""
        else:
            expanded_data_set = list(data_set)
            self.__field_access_prefix = "['"
            self.__field_access_postfix = "']"

        if look_for_correlations:
            expanded_data_set = self.find_correlations(expanded_data_set)

        # 2) recursively build branches or leaves based on best fit
        file += self.__build_branch(expanded_data_set, 1, ".root")

        file += ["    ", "    return tree"]
        self.__write_tree_file(file_name, file)


    def __build_branch(self, data_set: List[Dict], depth: int, branch_chain: str) -> List[str]:
        # 1) check that all labels are different
        labels_are_same, primary_label = self.check_labels(data_set)
        if labels_are_same or depth >= self.max_depth or len(data_set) <= self.min_node_size:
            return [f"    tree{branch_chain} = Leaf('{primary_label}')"]

        # 2) Find best field to split on and what value of it to split by
        file_additions = []

        max_gain = 0
        for field in data_set[0].keys():
            if field == self.label_name or not type(data_set[0][field]) in self.supported_field_types:
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
        if field_to_split_by[:10] == "self.MATH_": # Correlated fields
            value_to_split_by = field_to_split_by
        file_additions.append(f"    tree{branch_chain} = Branch(lambda x: x{self.__field_access_prefix}{field_to_split_by}{self.__field_access_postfix} <= {value_to_split_by})")

        # 5) Recursively build new branches
        depth+=1
        file_additions += self.__build_branch(left_data_set, depth, f"{branch_chain}.l")
        file_additions += self.__build_branch(right_data_set, depth, f"{branch_chain}.r")

        return file_additions

    
    def __write_tree_file(self, file_name: str, lines: List[str]) -> None:
        file = open(f"{file_name}.py", "w")
        for line in lines:
            file.write(line+"\n")
        file.close()


    def find_correlations(self, data_set: List[Dict]) -> List[Dict]:
        # 1 Get all fields we can work with
        fields = list(filter(lambda x: type(data_set[0][x]) in self.supported_field_types, data_set[0].keys()))
        
        # 2 get all pairs
        pairs = []
        for i, field in enumerate(fields):
            for other_field in fields[i+1:]:
                pairs.append((field, other_field))

        # 3 Add a field for the sum, diff, product, and quotient of each field.
        for item in data_set:
            for pair in pairs:
                for func in [self.MATH__SUM, self.MATH_DIFF, self.MATH_PROD, self.MATH_QUOT]:
                    # item key is the code to be written later
                    item[f"self.{str(func)[33:42]}(lambda x: x{self.__field_access_prefix}{pair[0]}{self.__field_access_postfix}, lambda x: x{self.__field_access_prefix}{pair[1]}{self.__field_access_postfix})"] = func(item[pair[0]], item[pair[1]])      
        
        return data_set


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
        
        return len(counted_labels.keys()) == 1, primary_label        


    def split_data(self, data_set: List[Dict], field_to_split_by: str, value_to_split_by) -> Tuple[List[Dict], List[Dict]]:
        left = []
        right = []
        for item in data_set:
            if item[field_to_split_by] <= value_to_split_by:
                left.append(item)
            else:
                right.append(item)

        return left, right


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

            if val == properties[i+1]: continue

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


    # Same functions used by BaseDecisionTree for duck typing
    def MATH__SUM(self, n1, n2) -> float:
        return n1+n2
    def MATH_DIFF(self, n1, n2) -> float:
        return n1-n2
    def MATH_PROD(self, n1, n2) -> float:
        return n1*n2
    def MATH_QUOT(self, n1, n2) -> float:
        """Divides n1 by n2 but returns n1 * 2**128 if n2 is zero."""
        if n2 == 0:
            return n1*340282366920938463463374607431768211456 # 2**128
        return n1+n2


