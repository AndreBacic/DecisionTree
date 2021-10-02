from BaseDecisionTree import *
from other_data import Shape

# class-like syntax because it acts like it's instantiating a class.
def ShapesCorrelationsTree2__545f25b2_c50d_48fd_8c00_931b29edf695() -> 'BaseDecisionTree':
    """
    ShapesCorrelationsTree2__545f25b2_c50d_48fd_8c00_931b29edf695 has been trained to identify the LABEL of a given object.
    """
    tree = BaseDecisionTree(None, object, 'ShapesCorrelationsTree2__545f25b2_c50d_48fd_8c00_931b29edf695')
    tree.root = Branch(lambda x: tree.MATH_PROD(x.width, x.height) <= 24.5)
    tree.root.l = Branch(lambda x: tree.MATH__SUM(x.width, x.height) <= 8.5)
    tree.root.l.l = Branch(lambda x: x.length <= 6.0)
    tree.root.l.l.l = Branch(lambda x: tree.MATH_DIFF(x.length, x.width) <= -1.5)
    tree.root.l.l.l.l = Leaf('rod')
    tree.root.l.l.l.r = Branch(lambda x: tree.MATH_DIFF(x.length, x.height) <= -1.0)
    tree.root.l.l.l.r.l = Branch(lambda x: x.width <= 2.5)
    tree.root.l.l.l.r.l.l = Leaf('rod')
    tree.root.l.l.l.r.l.r = Leaf('cuboid')
    tree.root.l.l.l.r.r = Branch(lambda x: x.length <= 2.5)
    tree.root.l.l.l.r.r.l = Leaf('cube')
    tree.root.l.l.l.r.r.r = Branch(lambda x: x.width <= 3.5)
    tree.root.l.l.l.r.r.r.l = Leaf('plane')
    tree.root.l.l.l.r.r.r.r = Leaf('cube')
    tree.root.l.l.r = Leaf('rod')
    tree.root.l.r = Leaf('cuboid')
    tree.root.r = Branch(lambda x: tree.MATH_PROD(x.length, x.height) <= 32.5)
    tree.root.r.l = Leaf('plane')
    tree.root.r.r = Branch(lambda x: x.width <= 7.0)
    tree.root.r.r.l = Branch(lambda x: x.length <= 9.5)
    tree.root.r.r.l.l = Leaf('rod')
    tree.root.r.r.l.r = Leaf('plane')
    tree.root.r.r.r = Leaf('cube')
    
    return tree


t = ShapesCorrelationsTree2__545f25b2_c50d_48fd_8c00_931b29edf695()
l = t.classify_one(Shape("", 8, 8, 8)) # works
f = t.classify_one(Shape("", 5, 5, 5)) # doesn't work 😢 'plane'
print(l, f)
print(t.classify_one(Shape("", 40, 1, 1)))
print(t.classify_one(Shape("", 1, 40, 1)))
print(t.classify_one(Shape("", 1, 1, 40)))