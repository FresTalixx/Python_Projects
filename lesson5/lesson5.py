class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} щось каже"


class Dog(Animal):  # Успадкування
    def bark(self):
        return f"{self.name} голосно гавкає"


animal = Animal("Тварина")
print(animal.speak())

dog = Dog("Собака")
print(dog.speak())
print(dog.bark())


class BreedDog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  # щоб не було конфліктів з name у класі Animal
        self.breed = breed

    def speak(self):
        # Виклик speak() з класу Animal
        return f"{super().speak()} і {self.name} є {self.breed}"  # Зразу 2 функції speak без помилки. Це є метод super


breed_dog = BreedDog("Собака", "Дог")
print(breed_dog.speak())


class MyClass:
    def __init__(self, value, name):
        self.name = name
        self.__my_private_def(value)

    def __my_private_def(self, value):
        print(f"Private method called with value: {value}")
        print(self.name)


obj = MyClass(54,"You")
