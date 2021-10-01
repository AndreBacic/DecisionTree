from BaseDecisionTree import *

# class-like syntax because it acts like it's instantiating a class.
def DecisionTreeModel__0391c9aa_3353_4a21_a215_7cb244169597() -> 'BaseDecisionTree':
    """
    DecisionTreeModel__0391c9aa_3353_4a21_a215_7cb244169597 has been trained to identify the species of a given dictionary object.
    """
    tree = BaseDecisionTree(None, dict, 'DecisionTreeModel__0391c9aa_3353_4a21_a215_7cb244169597')
    tree.root = Branch(lambda x: x['sepal_length'] <= 5.5)
    tree.root.l = Leaf('setosa')
    tree.root.r = Branch(lambda x: x['petal_length'] <= 5.0)
    tree.root.r.l = Leaf('versicolor')
    tree.root.r.r = Leaf('virginica')
    
    return tree
