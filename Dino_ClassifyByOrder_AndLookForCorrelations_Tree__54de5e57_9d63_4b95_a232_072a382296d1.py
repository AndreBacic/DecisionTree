from BaseDecisionTree import *

# class-like syntax because it acts like it's instantiating a class.
def Dino_ClassifyByOrder_AndLookForCorrelations_Tree__54de5e57_9d63_4b95_a232_072a382296d1() -> 'BaseDecisionTree':
    """
    Dino_ClassifyByOrder_AndLookForCorrelations_Tree__54de5e57_9d63_4b95_a232_072a382296d1 has been trained to identify the order of a given dictionary object.
    """
    tree = BaseDecisionTree(None, dict, 'Dino_ClassifyByOrder_AndLookForCorrelations_Tree__54de5e57_9d63_4b95_a232_072a382296d1')
    tree.root = Branch(lambda x: x['fingers per hand'] <= 3.5)
    tree.root.l = Leaf('Therapod')
    tree.root.r = Branch(lambda x: x['neck length (feet)'] <= 7.5)
    tree.root.r.l = Branch(lambda x: x['length (feet)'] <= 31.5)
    tree.root.r.l.l = Branch(lambda x: x['neck length (feet)'] <= 2.4)
    tree.root.r.l.l.l = Leaf('Marginocephalian')
    tree.root.r.l.l.r = Leaf('Thyreophoran')
    tree.root.r.l.r = Leaf('Ornithopod')
    tree.root.r.r = Leaf('Sauropod')
    
    return tree
