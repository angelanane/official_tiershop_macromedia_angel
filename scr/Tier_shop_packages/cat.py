from animals import Animal

class Cat(Animal):
    def __init__(self, id, name, race, gender, age, color, height, weight, price):
        super().__init__(id, name, race, gender, age, color, height, weight, price)

    def meow(self):
        pass

    def makes_noise(self):
        self.meow()
