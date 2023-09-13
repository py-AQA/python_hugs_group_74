# Мемоизация — оптимизационная техника,
# используемая для ускорения программ путем кэширования результатов дорогостоящих вызовов функций и возвращения кэшированного результата при повторных вызовах с теми же аргументами.

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))  # Без мемоизации это может занять довольно много времени

# Для большинства задач мемоизации рекомендуется использовать готовый декоратор functools.lru_cache, так как он предоставляет дополнительные возможности и оптимизации. Например:
from functools import lru_cache


@lru_cache(maxsize=None)  # maxsize=None означает неограниченный кэш
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))
# Тут lru_cache обеспечивает те же преимущества в производительности, что и наш пользовательский декоратор memoize.
