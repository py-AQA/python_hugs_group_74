from functools import wraps


def repeat(n, wrap=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        @wraps(func)
        def wraps_wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return [wrapper, wraps_wrapper][wrap]

    return decorator


@repeat(n=2, wrap=True)
def foo(x: int, y) -> None:
    """f_foo_doc"""
    print(x + y)


@repeat(n=2, wrap=False)
def bar(x: int, y) -> None:
    """f_bar_doc"""
    print(x + y)


print(foo, foo.__name__, foo.__doc__, foo.__dict__, foo.__module__, foo.__qualname__, foo.__annotations__, sep='\n')
print('---')
print(bar, bar.__name__, bar.__doc__, bar.__dict__, bar.__module__, bar.__qualname__, bar.__annotations__, sep='\n')
print('---')
foo(111, 1000)
bar(222, 2000)
