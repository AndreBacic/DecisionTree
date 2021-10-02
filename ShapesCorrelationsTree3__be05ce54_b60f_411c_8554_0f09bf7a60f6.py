from BaseDecisionTree import *
from other_data import Shape

# class-like syntax because it acts like it's instantiating a class.
def ShapesCorrelationsTree3__be05ce54_b60f_411c_8554_0f09bf7a60f6() -> 'BaseDecisionTree':
    """
    ShapesCorrelationsTree3__be05ce54_b60f_411c_8554_0f09bf7a60f6 has been trained to identify the LABEL of a given object.
    """
    tree = BaseDecisionTree(None, object, 'ShapesCorrelationsTree3__be05ce54_b60f_411c_8554_0f09bf7a60f6')
    tree.root = Branch(lambda x: tree.MATH_DIFF(x.length, x.width) <= 0.5)
    tree.root.l = Branch(lambda x: tree.MATH_DIFF(x.length, x.width) <= -0.5)
    tree.root.l.l = Branch(lambda x: tree.MATH_DIFF(x.length, x.height) <= -2.5)
    tree.root.l.l.l = Branch(lambda x: x.length <= 12.5)
    tree.root.l.l.l.l = Branch(lambda x: tree.MATH_DIFF(x.width, x.height) <= 3.5)
    tree.root.l.l.l.l.l = Leaf('plane')
    tree.root.l.l.l.l.r = Leaf('cuboid')
    tree.root.l.l.l.r = Leaf('cuboid')
    tree.root.l.l.r = Branch(lambda x: x.width <= 29.5)
    tree.root.l.l.r.l = Branch(lambda x: tree.MATH__SUM(x.length, x.height) <= 5.0)
    tree.root.l.l.r.l.l = Leaf('rod')
    tree.root.l.l.r.l.r = Leaf('cuboid')
    tree.root.l.l.r.r = Leaf('rod')
    tree.root.l.r = Branch(lambda x: tree.MATH_DIFF(x.length, x.height) <= -1.0)
    tree.root.l.r.l = Leaf('rod')
    tree.root.l.r.r = Branch(lambda x: tree.MATH_DIFF(x.length, x.height) <= 1.0)
    tree.root.l.r.r.l = Leaf('cube')
    tree.root.l.r.r.r = Leaf('plane')
    tree.root.r = Branch(lambda x: tree.MATH_DIFF(x.width, x.height) <= -8.0)
    tree.root.r.l = Leaf('plane')
    tree.root.r.r = Branch(lambda x: tree.MATH_DIFF(x.width, x.height) <= -1.0)
    tree.root.r.r.l = Branch(lambda x: x.width <= 2.0)
    tree.root.r.r.l.l = Branch(lambda x: x.length <= 3.0)
    tree.root.r.r.l.l.l = Leaf('cuboid')
    tree.root.r.r.l.l.r = Leaf('plane')
    tree.root.r.r.l.r = Leaf('cuboid')
    tree.root.r.r.r = Branch(lambda x: tree.MATH_DIFF(x.width, x.height) <= 1.0)
    tree.root.r.r.r.l = Leaf('rod')
    tree.root.r.r.r.r = Leaf('cuboid')
    
    return tree

t = ShapesCorrelationsTree3__be05ce54_b60f_411c_8554_0f09bf7a60f6()
labels = t.classify_many([
    Shape("", 8, 8, 8), # good
    Shape("", 5, 5, 5), # good
    Shape("", 1, 8, 1), # good
    Shape("", 8, 3, 3), # good
    Shape("", 80, 8, 80), # good
    Shape("", 3, 3, 1), # good
    Shape("", 8, 9, 80), # no; says'plane'
    Shape("", 6, 5, 4), # no; says 'rod'
])
for l in labels:
    print(l)