# Aleksi Kesälä
class Mammal:
    def __init__(self, name, age, gender, habitat):
        self.name = name
        self.age = age
        self.gender = gender
        self.habitat = habitat
        habitat.add_inhabitants(self)
    
    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")

    def move(self):
        print("Moving")


class Cat(Mammal):
    def __init__(self, name, age, gender, habitat, breed):
        super().__init__(name, age, gender, habitat)
        self.breed = breed

    def meow(self):
        print("meow")


class Dog(Mammal):
    def __init__(self, name, age, gender, habitat, breed):
        super().__init__(name, age, gender, habitat)
        self.breed = breed

    def bark(self):
        print("Bark bark!")


class Mouse(Mammal):
    def __init__(self, name, age, gender, habitat, breed):
        super().__init__(name, age, gender, habitat)
        self.breed = breed

    def squeek(self):
        print("Squeeeeeeek!")


class Elephant(Mammal):
    def __init__(self, name, age, gender, habitat, breed):
        super().__init__(name, age, gender, habitat)
        self.breed = breed

    def stomp(self):
        print("Stomps!")


class Rat(Mammal):
    def __init__(self, name, age, gender, habitat, breed):
        super().__init__(name, age, gender, habitat)
        self.breed = breed

    def steal(self):
        print("Stealing food")


class Habitat:
    def __init__(self, name, climate, vegetation, location, water_sources, terrain, fauna):
        self.name = name
        self.climate = climate
        self.vegetation = vegetation
        self.location = location
        self.water_sources = water_sources
        self.terrain = terrain
        self.fauna = fauna
        self.inhabitants = []

    def add_inhabitants(self, mammal):
        self.inhabitants.append(mammal)
#
