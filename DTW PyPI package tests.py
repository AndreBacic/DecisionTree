from decision_tree_writer import DecisionTreeWriter
from other_data import *

writer = DecisionTreeWriter(label_name="LABEL")

# Trains a new model and saves it to a new .py file.
writer.create_tree(data_set = shapes, 
                   look_for_correlations = True, 
                   data_set_is_certainly_comparable=True,
                   tree_name = "-3D Shape Classifier")