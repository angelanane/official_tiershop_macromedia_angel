from animals import Animal

class Dog(Animal):
    def __init__(self, id, name, race, gender, age, color, height, weight, price):
        super().__init__(id, name, race, gender, age, color, height, weight, price)

    def bark(self):
        pass

    def makes_noise(self):
        self.bark()
