# Aleksi Kesälä

class Mammal:
    def __init__(self):
        self.state = "Resting"

    def report_state(self):
        print(f"The mammal is currently: {self.state}")

    def hunger(self):
        if self.state == "Resting":
            self.state = "Hunting"
            print("The mammal has become hungry and starts hunting.")

    def sees_prey(self):
        if self.state == "Hunting":
            print("The mammal sees prey and continues hunting.")

    def caught_prey(self):
        if self.state == "Hunting":
            self.state = "Eating"
            print("The mammal has caught prey and starts eating.")

    def finishes_eating(self):
        if self.state == "Eating":
            self.state = "Resting"
            print("The mammal has finished eating and goes back to resting.")

    def thirsty_after_eating(self):
        if self.state == "Eating":
            self.state = "Searching for Water"
            print("The mammal is thirsty after eating and starts searching for water.")

    def thirsty(self):
        if self.state == "Resting":
            self.state = "Searching for Water"
            print("The mammal is thirsty and starts searching for water.")

    def water_found(self):
        if self.state == "Searching for Water":
            self.state = "Resting"
            print("The mammal has found water and goes back to resting.")

    def hunting_fails(self):
        if self.state == "Hunting":
            self.state = "Resting"
            print("The mammal failed to catch prey and goes back to resting.")


# testing code
mammal = Mammal()
mammal.report_state()
mammal.hunger()
mammal.report_state()
mammal.hunting_fails()
mammal.report_state()
mammal.water_found() # works.
mammal.report_state()
