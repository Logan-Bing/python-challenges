class Car:
    def __init__(self, model, color, collection=None):
        self.model = model
        self.color = color
        self.collection = collection if collection is not None else []

    def __str__(self):
        return f"Model : {self.model} de couleur {self.color}"

    def __repr__(self):
        return f"Car({repr(self.model)}, {repr(self.color)})"

    def __len__(self):
        return len(self.model)


car1 = Car("porsche", "full black")
print(len(car1))
print(repr(car1))
