result = []


def divider(a, b):
    if b == 0:
        raise ZeroDivisionError("Не можна ділити на 0")
    if b > 100:
        raise IndexError("b не може бути більне за 100")
    return a / b


data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print("Помилка, число b дорівнює 0")
    except IndexError:
        print("Помилка, b більше за 100")

print(result)
