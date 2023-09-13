# Когда вызывается функция slow_function, декоратор timing_decorator измеряет время,
# которое ушло на её выполнение, и выводит это время в консоль
from time import time, sleep


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed_time:.6f} секунд.")
        return result

    return wrapper


@timing_decorator
def slow_function(duration):
    sleep(duration)
    return duration


slow_function(2)
