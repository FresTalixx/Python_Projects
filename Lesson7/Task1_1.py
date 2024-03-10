num1 = float(input("Введіть 1 число:"))
num2 = float(input("Введіть 2 число:"))

try:
    num1 / num2
except ZeroDivisionError:
    print("На нуль не можна ділити")


