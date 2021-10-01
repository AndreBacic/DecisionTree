from BaseDecisionTree import *

# class-like syntax because it acts like its instantiating a class.
def DinoClassifyByOrderTree__cf5e3d7c_1df1_4a47_81e3_dce2d29dac4a() -> 'BaseDecisionTree':
    """
    DinoClassifyByOrderTree__cf5e3d7c_1df1_4a47_81e3_dce2d29dac4a has been trained to identify the order of a given dictionary object.
    """
    tree = BaseDecisionTree(None, dict, 'DinoClassifyByOrderTree__cf5e3d7c_1df1_4a47_81e3_dce2d29dac4a')
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
