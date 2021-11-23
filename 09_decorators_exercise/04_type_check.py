from functools import wraps


def type_check(type_to_check):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, type_to_check):
                return "Bad Type"
            return func(arg)
        return wrapper
    return decorator



@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
