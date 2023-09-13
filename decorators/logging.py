import functools
import time
from random import randint
from time import time, sleep


# import logging

# Настройка логирования
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# Декоратор для логирования
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}.")
        start_time = time()
        # Вызов оборачиваемой функции
        result = func(*args, **kwargs)
        end_time = time()
        duration = end_time - start_time
        print(f"Функция {func.__name__} завершилась за {duration} сек. и вернула {result}.")
        return result

    return wrapper


# При вызове функций add и multiply, информация о вызове и результате записывается в лог
@log_decorator
def add(a, b):
    return a + b


@log_decorator
def multiply(a, b):
    return a * b


@log_decorator
def hello_world():
    print("Hello world!")
    # Случайная пауза от 1 до 4 секунд
    случайная_пауза = randint(1, 5)
    print(f"Случайная пауза: {случайная_пауза} сек.")
    sleep(случайная_пауза)


@log_decorator
def sort_list(l: list):
    return sorted(l)


print(f"{add(3, 4)}")
multiply(4, 5)
hello_world()
sort_list([290, 21, 245])
