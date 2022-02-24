# Creates classes that instantiate a built tree model and test it against a given data set

from other_data import Shape


def test_IrisClassifier():
    from IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5 import IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5

    iris_classifier = IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5()

    sp = iris_classifier.classify_one({"sepal_length": 5.7, "sepal_width": 2.9, "petal_length": 4.2, "petal_width": 1.3})
    print(sp, "Should Be 'versicolor'")

def test__3D_Shape_Classifier():
    from _3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282 import _3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282

    shape_classifier = _3D_Shape_Classifier__978f3d1f_a1e5_4ca0_8ace_77790fd5a282()

    print(shape_classifier.classify_many([
        Shape("", 13, 13, 13),
        Shape("", 3, 4, 5),
        Shape("", 300, 0, 300),
        Shape("", 4, 4, 100)
    ]), "Should be ['cube', 'cuboid', 'plane', 'rod']")

test__3D_Shape_Classifier()