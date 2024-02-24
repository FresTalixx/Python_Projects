class Cat:
    def __init__(self, name, satiety, health, sleep):
        self.name = name
        self.sleep_level = sleep
        self.satiety_level = satiety
        self.health_level = health
        print("Working")

    def update_health(self, num):
        self.health_level += num

    def update_hunger(self, num):
        self.satiety_level += num

    def update_sleep(self, num):
        self.sleep_level += num


name0 = input("Введіть ім'я вашого кота: ")
satiety0 = 100
health0 = 100
sleep0 = 100

printText = "H - Підтримувати стан здоров'я, S - спати, E - Їсти"

cat = Cat(name0, satiety0, health0, sleep0)
while True:
    print(printText)
    ask = input("Що ви хочете зробити з вашим котом: ")

    if ask == "H" or ask == "h":
        askHealth = int(input("Наскільки ви хочете підтримати стан здоров'я: "))

        if askHealth <= 40:
            cat.update_hunger(-10)
            cat.update_sleep(-20)
        else:
            cat.update_hunger(15)
            cat.update_sleep(-13)

        print("Ситість: ", cat.satiety_level)
        print("Стан здоров'я: ", cat.health_level)
        print("Сон: ", cat.sleep_level)

    elif ask == "S" or ask == "s":
        askSleep = int(input("Скільки ви хочете спати(год): "))

        if askSleep <= 10:
            cat.update_hunger(-10)
            cat.update_health(-25)
        else:
            cat.update_hunger(15)
            cat.update_health(19)

        print("Ситість: ", cat.satiety_level)
        print("Стан здоров'я: ", cat.health_level)
        print("Сон: ", cat.sleep_level)

    elif ask == "E" or ask == "e":
        askEat = int(input("Скільки ви хочете їсти: "))

        if askEat <= 30:
            cat.update_sleep(-16)
            cat.update_health(-23)
        else:
            cat.update_hunger(18)
            cat.update_health(13)

        print("Ситість: ", cat.satiety_level)
        print("Стан здоров'я: ", cat.health_level)
        print("Сон: ", cat.sleep_level)

    else:
        print("Неправильна команда, введіть щераз")

    if cat.health_level <= 34 or cat.sleep_level <= 43 or cat.satiety_level <= 24:
        print("Ваш кіт помер(((")
        break



