class Car:
    def __init__(self, fuel: int = 30, speed: int = 100):
        self.fuel = fuel
        self.speed = speed

    def increase_speed(self, speed_increase: int = 20):
        self.speed += speed_increase

    def charge(self, fuel):
        self.fuel += fuel

    def drive(self, person):
        if person.age < 18:
            print(f"{person.name} ще неповнолітній(а), ви ще не можете водити авто")
        else:
            print(f"{person.name} водить авто зі швидкістю {self.speed} км/год")

    def print_info(self):
        print(f"Пальне:{self.fuel}")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))

person1 = Human(name, age)
car1 = Car()

car1.drive(person1)
car1.print_info()
