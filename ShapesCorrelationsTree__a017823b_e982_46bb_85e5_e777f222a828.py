from BaseDecisionTree import *
from other_data import Shape

# class-like syntax because it acts like it's instantiating a class.
def ShapesCorrelationsTree__a017823b_e982_46bb_85e5_e777f222a828() -> 'BaseDecisionTree':
    """
    ShapesCorrelationsTree__a017823b_e982_46bb_85e5_e777f222a828 has been trained to identify the LABEL of a given object.
    """
    tree = BaseDecisionTree(None, object, 'ShapesCorrelationsTree__a017823b_e982_46bb_85e5_e777f222a828')
    tree.root = Branch(lambda x: tree.MATH_DIFF(x.length, x.width) <= -3.0)
    tree.root.l = Leaf('plane')
    tree.root.r = Branch(lambda x: x.width <= 2.5)
    tree.root.r.l = Branch(lambda x: tree.MATH__SUM(x.length, x.height) <= 5.5)
    tree.root.r.l.l = Leaf('cube')
    tree.root.r.l.r = Branch(lambda x: tree.MATH_PROD(x.length, x.height) <= 13.0)
    tree.root.r.l.r.l = Leaf('rod')
    tree.root.r.l.r.r = Leaf('plane')
    tree.root.r.r = Branch(lambda x: x.length <= 1.5)
    tree.root.r.r.l = Leaf('rod')
    tree.root.r.r.r = Branch(lambda x: x.length <= 5.5)
    tree.root.r.r.r.l = Leaf('cylinder')
    tree.root.r.r.r.r = Leaf('cube')
    
    return tree

t = ShapesCorrelationsTree__a017823b_e982_46bb_85e5_e777f222a828()
l = t.classify_one(Shape("", 8, 8, 8)) # works
f = t.classify_one(Shape("", 5, 5, 5)) # doesn't work 😢
print(l, f)