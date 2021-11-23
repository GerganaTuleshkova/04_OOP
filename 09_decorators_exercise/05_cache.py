from functools import wraps


def cache(func):
    cache_dict = {}

    @wraps(func)
    def wrapper(arg):
        key = arg
        value = func(arg)
        if key not in cache_dict:
            cache_dict[key] = value
        return value
    wrapper.log = cache_dict
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


(fibonacci(4))
print(fibonacci.log)
