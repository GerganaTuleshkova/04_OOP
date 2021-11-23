from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            result = function(*args)
            return result * times
        return wrapper
    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
print(add_ten(3))
