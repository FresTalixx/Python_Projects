print("Hello world")


class Cat:
    def __init__(self, name, hunger, size):
        self.name = name
        self.hunger = hunger
        self.size = size
        print("Working")

    def grow(self):
        self.size += 1

    def hunger(self):
        self.hunger += 1

     def satiety(self):
        self.hunger -= 1

