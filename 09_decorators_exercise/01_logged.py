from functools import wraps


def logged(function_ref):
    @wraps(function_ref)
    def wrapper(*args):
        result_string = f"you called {function_ref.__name__}{args}\n" \
                        f"it returned {function_ref(*args)}"
        return result_string
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))


print(func(4, 4, 4))
