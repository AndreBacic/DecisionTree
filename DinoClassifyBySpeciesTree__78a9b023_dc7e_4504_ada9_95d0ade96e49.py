from BaseDecisionTree import *

# class-like syntax because it acts like it's instantiating a class.
def DinoClassifyBySpeciesTree__78a9b023_dc7e_4504_ada9_95d0ade96e49() -> 'BaseDecisionTree':
    """
    DinoClassifyBySpeciesTree__78a9b023_dc7e_4504_ada9_95d0ade96e49 has been trained to identify the species of a given dictionary object.
    """
    tree = BaseDecisionTree(None, dict, 'DinoClassifyBySpeciesTree__78a9b023_dc7e_4504_ada9_95d0ade96e49')
    tree.root = Branch(lambda x: x['length (feet)'] <= 68.5)
    tree.root.l = Branch(lambda x: x['length (feet)'] <= 31.0)
    tree.root.l.l = Branch(lambda x: x['length (feet)'] <= 14.0)
    tree.root.l.l.l = Leaf('Oviraptor')
    tree.root.l.l.r = Branch(lambda x: x['length (feet)'] <= 26.0)
    tree.root.l.l.r.l = Leaf('Pachycephalosaurus')
    tree.root.l.l.r.r = Branch(lambda x: x['height (feet)'] <= 9.85)
    tree.root.l.l.r.r.l = Branch(lambda x: x['length (feet)'] <= 29.5)
    tree.root.l.l.r.r.l.l = Leaf('Shunosaurus')
    tree.root.l.l.r.r.l.r = Leaf('Ankylosaurus')
    tree.root.l.l.r.r.r = Branch(lambda x: x['height (feet)'] <= 12.85)
    tree.root.l.l.r.r.r.l = Leaf('Triceratops')
    tree.root.l.l.r.r.r.r = Leaf('Stegosaurus')
    tree.root.l.r = Branch(lambda x: x['length (feet)'] <= 32.5)
    tree.root.l.r.l = Leaf('Therizinosaurus')
    tree.root.l.r.r = Branch(lambda x: x['length (feet)'] <= 42.0)
    tree.root.l.r.r.l = Branch(lambda x: x['length (feet)'] <= 37.0)
    tree.root.l.r.r.l.l = Leaf('Parasaurolophus')
    tree.root.l.r.r.l.r = Leaf('Tyrannosaurus')
    tree.root.l.r.r.r = Branch(lambda x: x['length (feet)'] <= 47.5)
    tree.root.l.r.r.r.l = Leaf('Iguanodon')
    tree.root.l.r.r.r.r = Leaf('Spinosaurus')
    tree.root.r = Branch(lambda x: x['length (feet)'] <= 87.0)
    tree.root.r.l = Leaf('Brachiosaurus')
    tree.root.r.r = Leaf('Diplodocus')
    
    return tree
