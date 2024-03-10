num1 = input("Введіть число: ")

try:
    num1 = float(num1)
except ValueError:
    print("Ви ввели не число")
