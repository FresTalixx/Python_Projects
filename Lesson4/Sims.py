import random


class Human:

    def __init__(self, name: str = "Sim", age: int = 1, energy: int = 100, happiness: int = 100, hunger: int = 0):
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger

    def eat(self, food: int):
        self.hunger -= food
        if self.hunger <= 0:
            self.hunger = 0
        print(f"{self.name} поїв. Голод: {self.hunger}")

    def sleep(self, hours: int):
        self.energy += hours
        if self.energy >= 100:
            self.energy = 100
        print(f"{self.name} поспав. Енергія: {self.energy}")

    def play(self, activity: int):
        self.happiness += activity
        if self.happiness >= 100:
            self.happiness = 100
        print(f"{self.name} пограв. Радість: {self.happiness}")

    def grow_up(self, years: int = 1):
        self.age += years
        print(f"{self.name} подорослішав. Вік: {self.age}")

    def status(self):
        print(f"Статус {self.name}")
        print(f"Вік: {self.age}")
        print(f"Енергія: {self.energy}")
        print(f"Радість: {self.happiness}")
        print(f"Голод: {self.hunger}")


name1 = input("Введіть ім'я свого сіма: ")
sim1 = Human(name1)

while True:
    randNum = random.randint(1, 12)
    print("Е - їсти, С - спати, Г - грати")
    ask = input("Що ви хочете зробити зі своїм сімом: ")

    if ask == "Е" or ask == "е":
        askEat = int(input("Скільки хочете з'їсти їжі: "))
        sim1.eat(askEat)
    elif ask == "С" or ask == "с":
        askSleep = int(input("Скільки хочете спати годин:"))
        sim1.sleep(askSleep)
    elif ask == "Г" or ask == "г":
        askPlay = int(input("Скільки хочете грати:"))
        sim1.play(askPlay)
    else:
        print("Невірна команда")
    if randNum == 7:
        sim1.grow_up()

    sim1.status()
