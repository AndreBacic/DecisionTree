# This file if for testing the code in TreeBuilder.py and perhaps any other files that need testing

from TreeBuilder import DecisionTreeBuilder
from TreeWriter import DecisionTreeWriter
from dinosaur_data import Dinosaurs
import time

builder = DecisionTreeBuilder()

iris_data = [
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 3.5, "petal_length": 1.5, "petal_width": 0.2},
    { "species": "setosa", "sepal_length": 4.8, "sepal_width": 3.1, "petal_length": 1.6, "petal_width": 0.2},
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 4.1, "petal_length": 1.5, "petal_width": 0.1},
    { "species": "setosa", "sepal_length": 5.4, "sepal_width": 3.7, "petal_length": 1.5, "petal_width": 0.2},
    { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 3.0, "petal_length": 4.5, "petal_width": 1.5},
    { "species": "versicolor", "sepal_length": 6.2, "sepal_width": 2.2, "petal_length": 4.5, "petal_width": 1.5},
    { "species": "versicolor", "sepal_length": 5.7, "sepal_width": 2.9, "petal_length": 4.2, "petal_width": 1.3},
    { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 2.9, "petal_length": 3.6, "petal_width": 1.3},
    { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.6, "petal_length": 6.1, "petal_width": 2.5},
    { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.2, "petal_length": 6.0, "petal_width": 1.8},
    { "species": "virginica", "sepal_length": 6.1, "sepal_width": 2.6, "petal_length": 5.6, "petal_width": 1.4},
    { "species": "virginica", "sepal_length": 6.8, "sepal_width": 3.0, "petal_length": 5.5, "petal_width": 2.1},
    ]

def calculate_gini_impurity_Should_work(): # It works!
    print("calculate_gini_impurity() output and what it should be")
    print(builder.__calculate_gini_impurity([0, 0, 0]), "Should Be", 0)
    print(builder.__calculate_gini_impurity([0, 1]), "Should Be", 0.5)
    print(builder.__calculate_gini_impurity([0, 0, 0, 1]), "Should Be", 0.375)
    print(builder.__calculate_gini_impurity([0, 1, 2]), "Should Be", 0.6666667)
    print(builder.__calculate_gini_impurity([2, 1, 2]), "Should Be", 0.4444444)

def calculate_max_gini_gain_Should_work(): # It works!
    print("calculate_max_gini_gain() output and what it should be")
    print(builder.__calculate_max_gini_gain(["s", "c"], [1, 2]), "Should Be", (0.5, 1.5))
    print(builder.__calculate_max_gini_gain(["s", "s", "c"], [1, 2, 8]), "Should Be", (0.4444444, 5))
    print(builder.__calculate_max_gini_gain(["s", "h", "s", "c", "h"], [1, 2, 2, 8, 15]), "Should Be", (0.1733333, 5))

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
    for t in builder.__split_data(data, "s", 2):
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
    print(builder.__check_labels(data), "Should Be", (True, "Snake"))
    data[2]["LABEL"] = "Frog"
    print(builder.__check_labels(data), "Should Be", (False, "Snake"))
    data[0]["LABEL"] = "Frog"
    print(builder.__check_labels(data), "Should Be", (False, "Frog"))

def build_tree_Should_work(): # It works with the old way that returns a BaseDecisionTree object.
    builder.label_name = "species"
    tree = builder.build_tree(iris_data, "IrisClassifier")
    print(tree)
    setosa = tree.classify(iris_data[0])
    print(setosa)

writer = DecisionTreeWriter(label_name="species", min_node_size=1, max_depth=8)
t = time.time()
writer.build_tree(Dinosaurs, "DinoClassifyBySpeciesTree")
print(time.time()-t)