from BaseDecisionTree import *
from other_data import Shape

# class-like syntax because it acts like it's instantiating a class.
def ShapesCorrelationsTree3__35452ba1_bf10_4060_9d7f_fd19d20495d2() -> 'BaseDecisionTree':
    """
    ShapesCorrelationsTree3__35452ba1_bf10_4060_9d7f_fd19d20495d2 has been trained to identify the LABEL of a given object.
    """
    tree = BaseDecisionTree(None, Shape, 'ShapesCorrelationsTree3__35452ba1_bf10_4060_9d7f_fd19d20495d2')
    tree.root = Branch(lambda x: tree.MATH___EQ(x.length, x.width) <= 0.5)
    tree.root.l = Branch(lambda x: tree.MATH___EQ(x.length, x.height) <= 0.5)
    tree.root.l.l = Branch(lambda x: tree.MATH___EQ(x.width, x.height) <= 0.5)
    tree.root.l.l.l = Leaf('cuboid')
    tree.root.l.l.r = Branch(lambda x: x.length <= 6.5)
    tree.root.l.l.r.l = Leaf('plane')
    tree.root.l.l.r.r = Leaf('rod')
    tree.root.l.r = Branch(lambda x: tree.MATH_DIFF(x.length, x.width) <= 0.5)
    tree.root.l.r.l = Leaf('rod')
    tree.root.l.r.r = Leaf('plane')
    tree.root.r = Branch(lambda x: tree.MATH___EQ(x.length, x.height) <= 0.5)
    tree.root.r.l = Branch(lambda x: x.height <= 3.5)
    tree.root.r.l.l = Leaf('plane')
    tree.root.r.l.r = Leaf('rod')
    tree.root.r.r = Leaf('cube')
    
    return tree

t = ShapesCorrelationsTree3__35452ba1_bf10_4060_9d7f_fd19d20495d2()
labels = t.classify_many([
    Shape("", 8, 8, 8), # good
    Shape("", 5, 5, 5), # good
    Shape("", 1, 8, 1), # good
    Shape("", 8, 3, 3), # good
    Shape("", 80, 8, 80), # good
    Shape("", 3, 3, 1), # good
    Shape("", 8, 9, 80), # good
    Shape("", 6, 5, 4), # good
])
for l in labels:
    print(l) 

