# Мемоизация — оптимизационная техника,
# используемая для ускорения программ путем кэширования результатов дорогостоящих вызовов функций и возвращения кэшированного результата при повторных вызовах с теми же аргументами.
from decorators.timing_decorator import timing_decorator


def memoize(func):
    # Он сохраняется между вызовами нашей функции
    cache = {}  # Словарь для хранения результатов вычислений

    def wrapper(*args):
        # Если результат уже есть в кеше
        if args in cache:
            # то возвращаем результат из кеша
            return cache[args]
        # Если результатов нет в кеше, то вызываем функцию
        result = func(*args)
        # И запоминаем результат в кеше
        cache[args] = result
        # И возвращаем результат
        return result

    return wrapper


# Вычисление чисел Фибоначчи с помощью рекурсии
@memoize
def fibonacci(n: int):
    assert isinstance(n, int) and n >= 0, "n должно быть целым неотрицательным числом"
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timing_decorator
def call_fibonacci(n):
    return fibonacci(n)


print(call_fibonacci(36))  # Без мемоизации это может занять довольно много времени

# Для большинства задач мемоизации рекомендуется использовать готовый декоратор functools.lru_cache, так как он предоставляет дополнительные возможности и оптимизации. Например:
from functools import lru_cache


@lru_cache(maxsize=None)  # maxsize=None означает неограниченный кэш
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))
# Тут lru_cache обеспечивает те же преимущества в производительности, что и наш пользовательский декоратор memoize.
