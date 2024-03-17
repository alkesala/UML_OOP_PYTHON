# Aleksi Kesälä
class Mammal:
    def __init__(self, name):
        self.name = name

    def search_for_prey(self):
        print(f"{self.name} is searching for prey.")

    def detect_rabbit(self, rabbit):
        print(f"{self.name} has detected a rabbit {rabbit.name}.")

    def approach(self, rabbit):
        print(f"{self.name} approaches {rabbit.name}.")

    def catch(self, rabbit):
        print(f"{self.name} catches {rabbit.name}.")

    def eat(self, rabbit):
        print(f"{self.name} eats {rabbit.name}.")

    def rest(self):
        print(f"{self.name} rests.")


class Prey:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def caught_by(self, predator):
        self.is_alive = False
        print(f"{self.name} is caught by {predator.name}.")


class Habitat:
    def __init__(self, name):
        self.name = name


# code for testing
fox = Mammal("Fox")
rabbit = Prey("Rabbit")
forest = Habitat("Forest")

fox.search_for_prey()
fox.detect_rabbit(rabbit)
fox.approach(rabbit)
fox.catch(rabbit)
fox.eat(rabbit)
fox.rest()
