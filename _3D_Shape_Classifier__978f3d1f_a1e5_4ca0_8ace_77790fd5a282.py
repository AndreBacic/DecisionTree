from decision_tree_writer.BaseDecisionTree import *

# Please fix this import statement if necessary
from other_data import Shape

# class-like syntax because it acts like it's instantiating a class.
def _3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282() -> 'BaseDecisionTree':
    """
    _3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282 has been trained to identify the LABEL of a given Shape.
    """
    tree = BaseDecisionTree(None, Shape, '_3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282')
    tree.root = Branch(lambda x: tree.MATH_EQUALS(x.length, x.width) <= 0.5)
    tree.root.l = Branch(lambda x: tree.MATH_EQUALS(x.length, x.height) <= 0.5)
    tree.root.l.l = Branch(lambda x: tree.MATH_EQUALS(x.width, x.height) <= 0.5)
    tree.root.l.l.l = Leaf('cuboid')
    tree.root.l.l.r = Branch(lambda x: x.length <= 6.5)
    tree.root.l.l.r.l = Leaf('plane')
    tree.root.l.l.r.r = Leaf('rod')
    tree.root.l.r = Branch(lambda x: tree.MATH_DIFFERENCE(x.length, x.width) <= 0.5)
    tree.root.l.r.l = Leaf('rod')
    tree.root.l.r.r = Leaf('plane')
    tree.root.r = Branch(lambda x: tree.MATH_EQUALS(x.length, x.height) <= 0.5)
    tree.root.r.l = Branch(lambda x: x.height <= 3.5)
    tree.root.r.l.l = Leaf('plane')
    tree.root.r.l.r = Leaf('rod')
    tree.root.r.r = Leaf('cube')
    
    return tree
