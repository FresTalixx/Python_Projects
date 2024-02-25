password = input("Введіть пароль: ")
print("------------------------\n" * 100)

passwordAsk = input("Введіть свій пароль: ")

if passwordAsk == password:
    print("Пароль вірний")
else:
    print("Пароль невірний")
