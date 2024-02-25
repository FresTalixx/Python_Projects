def choco_game(n, m, k):
    square = n * m

    if k >= square:
        print("Неножна")
    elif k % n == 0 or k % m == 0:
        print("Можна")
    else:
        print("Неможна")


n1 = int(input("Введіть довжину шоколадки: "))
m1 = int(input("Введіть ширину шоколадки: "))
k1 = int(input("Введіть кількість відломів по прямій: "))

choco_game(n1, m1, k1)
