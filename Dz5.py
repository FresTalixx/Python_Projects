import colorama
from colorama import *

colorama.init(autoreset=True)  # коректно ініціалізую модуль , auto reset автоматично онуляє колір після
print(Fore.RED + Back.BLUE + Style.BRIGHT + 'Hello, World!', 'green', 'on_red')  # Fore(foreground) - текст
# Fore.Reset - онуляє колір (у на є авторесет)
# Back.BLUE - задній план
# Style.BRIGHT - яскравість



