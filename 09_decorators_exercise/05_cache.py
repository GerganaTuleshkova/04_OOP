from functools import wraps


def cache(func):
    cache_dict = {}

    @wraps(func)
    def wrapper(arg):
        if arg in cache_dict:
            return cache_dict[arg]
        result = func(arg)
        cache_dict[arg] = result
        return result

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
