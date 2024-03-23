import logging
from utils import name1

# Configure logging
logging.basicConfig(filename='example.log', level=logging.INFO)
logger = logging.getLogger(__name__)

name = name1


def eat():
    logger.info(f"{name} Поїв")
    print(f"{name} Поїв")


def sleep():
    logger.info(f"{name} Заснув")
    print(f"{name} Заснув")


def play():
    logger.info(f"{name} Пограв")
    print(f"{name} Пограв")


def grow_up():
    logger.info(f"{name} Виріс")
    print(f"{name} Виріс")


def status():
    logger.info(f"{name} подивився свій статус")
    print(f"{name} подивився свій статус")


def name_entered():
    logger.info(f"Користувач ввів ім'я {name}")
    print(f"Користувач ввів ім'я {name}")
