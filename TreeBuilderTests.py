# This file if for testing the code in TreeBuilder.py and perhaps any other files that need testing

from TreeBuilder import DecisionTreeBuilder
from TreeWriter import DecisionTreeWriter
from dinosaur_data import Dinosaurs
from other_data import *
import time

builder = DecisionTreeBuilder()


def calculate_gini_impurity_Should_work(): # It works!
    print("calculate_gini_impurity() output and what it should be")
    print(builder.calculate_gini_impurity([0, 0, 0]), "Should Be", 0)
    print(builder.calculate_gini_impurity([0, 1]), "Should Be", 0.5)
    print(builder.calculate_gini_impurity([0, 0, 0, 1]), "Should Be", 0.375)
    print(builder.calculate_gini_impurity([0, 1, 2]), "Should Be", 0.6666667)
    print(builder.calculate_gini_impurity([2, 1, 2]), "Should Be", 0.4444444)

def calculate_max_gini_gain_Should_work(): # It works!
    print("calculate_max_gini_gain() output and what it should be")
    print(builder.calculate_max_gini_gain(["s", "c"], [1, 2]), "Should Be", (0.5, 1.5))
    print(builder.calculate_max_gini_gain(["s", "s", "c"], [1, 2, 8]), "Should Be", (0.4444444, 5))
    print(builder.calculate_max_gini_gain(["s", "h", "s", "c", "h"], [1, 2, 2, 8, 15]), "Should Be", (0.1733333, 5))

def split_data_Should_work(): # It works!
    data = [{
        "s": 1,
        "n": 3
    }, {
        "s": 3,
        "n": 4
    },{
        "s": 2,
        "n": 5
    }]
    for t in builder.split_data(data, "s", 2):
        print(t) # good output

def check_labels_Should_work():
    data = [{
        "s": 1,
        "LABEL": "Snake"
    }, {
        "s": 3,
        "LABEL": "Snake"
    },{
        "s": 2,
        "LABEL": "Snake"
    }]
    print(builder.check_labels(data), "Should Be", (True, "Snake"))
    data[2]["LABEL"] = "Frog"
    print(builder.check_labels(data), "Should Be", (False, "Snake"))
    data[0]["LABEL"] = "Frog"
    print(builder.check_labels(data), "Should Be", (False, "Frog"))

def build_tree_Should_work(): # It works with the old way that returns a BaseDecisionTree object.
    builder.label_name = "species"
    tree = builder.build_tree(iris_data, "IrisClassifier")
    print(tree)
    setosa = tree.classify(iris_data[0])
    print(setosa)

writer = DecisionTreeWriter(min_node_size=1, max_depth=8)
t = time.time()
writer.build_tree(shapes, True,"ShapesCorrelationsTree")
print(time.time()-t)
# builder.label_name = "order"
# builder.build_tree(Dinosaurs)