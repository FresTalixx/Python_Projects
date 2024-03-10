list1 = [11, 2, 3, 5, 6, 7, "Cool"]

while True:
    index = int(input("Введіть індекс: "))

    try:
        print(list1[index])
    except IndexError:
        print("Такого елементу немає")
        break

