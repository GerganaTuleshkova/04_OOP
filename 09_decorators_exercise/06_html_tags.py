from functools import wraps


def tags(html_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = f"<{html_tag}>{func(*args)}</{html_tag}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
