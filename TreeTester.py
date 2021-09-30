# TODO: Create a class that instantiates a built tree model and tests it against a data set

from IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5 import IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5

iris_classifier = IrisClassifier__ce91b0eb_e0d8_4099_ad12_b890f93eb9b5()

sp = iris_classifier.classify({"sepal_length": 5.7, "sepal_width": 2.9, "petal_length": 4.2, "petal_width": 1.3})
print(sp, "Should Be 'versicolor'")