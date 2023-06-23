class Animal:
    def __init__(self, id, name, race, gender, age, color, height, weight, price):
        self.id = id
        self.name = name
        self.race = race
        self.gender = gender
        self.age = age
        self.color = color
        self.height = height
        self.weight = weight
        self.price = price

    def eat(self):
        pass

    def sleep(self):
        pass

    def makes_noise(self):
        pass

    def __str__(self):
        return f"Animal: {self.id}, Name: {self.name}, Race: {self.race}, Gender: {self.gender}, Age: {self.age}, Color: {self.color}, Height: {self.height}"
