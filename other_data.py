iris_data = [
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 3.5, "petal_length": 1.5, "petal_width": 0.2},
    { "species": "setosa", "sepal_length": 4.8, "sepal_width": 3.1, "petal_length": 1.6, "petal_width": 0.2},
    { "species": "setosa", "sepal_length": 5.2, "sepal_width": 4.1, "petal_length": 1.5, "petal_width": 0.1},
    { "species": "setosa", "sepal_length": 5.4, "sepal_width": 3.7, "petal_length": 1.5, "petal_width": 0.2},
    { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 3.0, "petal_length": 4.5, "petal_width": 1.5},
    { "species": "versicolor", "sepal_length": 6.2, "sepal_width": 2.2, "petal_length": 4.5, "petal_width": 1.5},
    { "species": "versicolor", "sepal_length": 5.7, "sepal_width": 2.9, "petal_length": 4.2, "petal_width": 1.3},
    { "species": "versicolor", "sepal_length": 5.6, "sepal_width": 2.9, "petal_length": 3.6, "petal_width": 1.3},
    { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.6, "petal_length": 6.1, "petal_width": 2.5},
    { "species": "virginica", "sepal_length": 7.2, "sepal_width": 3.2, "petal_length": 6.0, "petal_width": 1.8},
    { "species": "virginica", "sepal_length": 6.1, "sepal_width": 2.6, "petal_length": 5.6, "petal_width": 1.4},
    { "species": "virginica", "sepal_length": 6.8, "sepal_width": 3.0, "petal_length": 5.5, "petal_width": 2.1},
    ]

class Shape:
    def __init__(self, label, length, width, height) -> None:
        self.LABEL = label
        self.length = length
        self.width = width
        self.height = height

shapes = [
    Shape("cube", 1, 1, 1),
    Shape("cube", 2, 2, 2),
    Shape("cube", 6, 6, 6),
    Shape("rod", 9, 1, 1),
    Shape("rod", 2, 2, 5),
    Shape("rod", 1, 3, 1),
    Shape("plane", 1, 10, 10),
    Shape("plane", 4, 1, 4),
    Shape("plane", 1, 5, 5),
    Shape("cylinder", 2, 4, 2),
    Shape("cylinder", 5, 4, 4),
    Shape("cylinder", 3, 3, 6),
]