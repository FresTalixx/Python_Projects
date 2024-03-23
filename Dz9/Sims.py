import random
import mylib
from mylib import *
import utils
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
        mylib.eat()
        logger.info("This is a test info message")

    def sleep(self, hours: int):
        self.energy += hours
        if self.energy >= 100:
            self.energy = 100
        print(f"{self.name} поспав. Енергія: {self.energy}")
        mylib.sleep()

    def play(self, activity: int):
        self.happiness += activity
        if self.happiness >= 100:
            self.happiness = 100
        print(f"{self.name} пограв. Радість: {self.happiness}")
        mylib.play()

    def grow_up(self, years: int = 1):
        self.age += years
        print(f"{self.name} подорослішав. Вік: {self.age}")
        mylib.grow_up()

    def status(self):
        print(f"Статус {self.name}")
        print(f"Вік: {self.age}")
        print(f"Енергія: {self.energy}")
        print(f"Радість: {self.happiness}")
        print(f"Голод: {self.hunger}")
        mylib.status()


name1 = utils.name1
sim1 = Human(name1)


def main():
    logging.basicConfig(filename="Sims_log", level=logging.INFO)
    logging.info("Logging has started")
    while True:
        rand_num = random.randint(1, 12)
        print("Е - їсти, С - спати, Г - грати")
        ask = input("Що ви хочете зробити зі своїм сімом: ")

        if ask == "Е" or ask == "е":
            ask_eat = int(input("Скільки хочете з'їсти їжі: "))
            sim1.eat(ask_eat)
            mylib.eat()
        elif ask == "С" or ask == "с":
            ask_sleep = int(input("Скільки хочете спати годин:"))
            sim1.sleep(ask_sleep)
        elif ask == "Г" or ask == "г":
            ask_play = int(input("Скільки хочете грати:"))
            sim1.play(ask_play)
        else:
            print("Невірна команда")
        if rand_num == 7:
            sim1.grow_up()

        sim1.status()
        logging.info("Logging has finished")

        global end
        end = input("Закінчити? - ")

        if end == "Так" or end == "так":
            break
        elif end == "Ні" or end == "ні":
            continue
        else:
            "Невірна команда"


if __name__ == '__main__':
    main()

