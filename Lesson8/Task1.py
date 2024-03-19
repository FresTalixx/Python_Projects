list1 = [6, 5, 88, 4, "23"]

def error_fix(func):
    def inner(list0):
        userIndexInput = int(input("Введіть індекс: "))
        if userIndexInput >= len(list0):
            print("Немає такого індексу")
            return
        return func(list0)
    return inner

@error_fix
def print_list(list0):
    return list0


check_index = print_list(list1)

