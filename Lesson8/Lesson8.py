def iter_numbers():
    for j in range(10):
        yield j


iterator = iter_numbers()

for i in iterator:
    print(i)


def func_gen():
    i = 0
    while True:
        yield i
        i += 1


f = func_gen()
print(f)

f1 = (i for i in range(50))
print(f1)
print(next(f1))
print(next(f1))


def test_range():
    for i in range(0, 1):
        yield i


i = test_range()
print(next(i))


def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 1
        return x

    return inner_function()


function = outer_function()

print(function)


def guard_zero(operate):
    def inner(x, y):
        if y == 0:
            print("Can't divide by zero")
            return
        return operate(x, y)

    return inner


@guard_zero
def divide(x, y):
    return x / y


print(divide(5, 0))
