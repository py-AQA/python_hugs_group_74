from functools import wraps


def repeat(n):
    def _repeat(n):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for i in range(n):
                    func(*args, **kwargs)

            return wrapper

        return decorator


@repeat(n=5)
def foo(x, y):
    print(x + y)


print(foo)
foo(324, 1000)
