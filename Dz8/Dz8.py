class GenIter:
    def __init__(self, number):
        self.num = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 50:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration


number = int(input("Введіть число: "))
myclass = GenIter(number)

for num in myclass:
    print(num)
