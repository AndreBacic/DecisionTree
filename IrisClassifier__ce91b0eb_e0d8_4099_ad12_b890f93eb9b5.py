from BaseDecisionTree import *

# class-like syntax because it acts like its instantiating a class.
def IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5() -> 'BaseDecisionTree':
    """
    IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5 has been trained to identify the species of a given dictionary object.
    """
    tree = BaseDecisionTree(None, dict, 'IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5')
    tree.root = Branch(lambda x: x['sepal_length'] <= 5.5)
    tree.root.l = Leaf('setosa')
    tree.root.r = Branch(lambda x: x['petal_length'] <= 5.0)
    tree.root.r.l = Leaf('versicolor')
    tree.root.r.r = Leaf('virginica')
    
    return tree
