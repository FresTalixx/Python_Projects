import warnings
print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

a = 1
b = 0

try:
    a / b
except ZeroDivisionError:
    print("Не можна ділити на нуль")

try:
    f = open('file.txt', "r")

except FileNotFoundError:
    print("Файл не знайдено")

warnings.warn("Warning, no code here", SyntaxWarning)

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)
warnings.simplefilter("default", UserWarning)
warnings.simplefilter("error", RuntimeWarning)
warnings.simplefilter("module", ResourceWarning)
warnings.simplefilter("once", EncodingWarning)

warnings.warn("Warning, missed line of code", SyntaxWarning)
warnings.warn("Warning, module not import", ImportWarning)

warnings.warn("Warning, missed line of code", SyntaxWarning)
try:
    warnings.warn("Warning, module not import", ImportWarning)
except Warning:
    print("Warning processed")
