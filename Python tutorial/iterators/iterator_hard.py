mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 3
        return self

    def __next__(self):
        if self.a <= 31:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for numbers in myiter:
    print(numbers)
