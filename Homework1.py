print("Hello world")


class Cat:
    def __init__(self, name, hunger, size):
        self.name = name
        self.hunger = 0
        self.size = 1
        print("Working")

    def grow(self):
        self.size += 1

    def hunger(self):
        self.hunger += 5

    def satiety(self):
        self.hunger -= 5

cat1 = Cat()
while True:
    ask = input("Що ви хочете зробити з вашим котом - ")





