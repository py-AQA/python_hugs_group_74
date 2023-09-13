def lazy(n: int):
    assert n != 0, "n не должно быть равно 0"

    def decorator(func):
        decorator.count = 0

        def wrapper(*args, **kwargs):
            decorator.count += 1
            # print(f"Функция {func.__name__} вызвана {decorator.count} раз")
            if n == 1:
                return func(*args, **kwargs)
            if n > 1:
                return func(*args, **kwargs) if decorator.count % n == 1 else None
            if n < 0:
                return func(*args, **kwargs) if decorator.count % abs(n) != 0 else None

        return wrapper

    return decorator


@lazy(1)
def half1(x):
    return x / 2


assert half1(10) == 5
assert half1(8) == 4
assert half1(24) == 12
assert half1(1000) == 500


@lazy(4)
def half(x):
    return x // 2


assert half(10) == 5
assert half(77) is None
assert half(63) is None
assert half(2) is None
assert half(38) == 19


@lazy(-3)
def output_str(s):
    return s


assert output_str('Foo') == 'Foo'
assert output_str('Bar') == 'Bar'
assert output_str('Pikachu') is None
assert output_str('Gla') == 'Gla'
