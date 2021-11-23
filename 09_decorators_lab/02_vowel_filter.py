import functools


def vowel_filter(function):

    @functools.wraps(function)
    def wrapper():
        result = function()
        return [x for x in result if x.lower() in "aeiouy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
print(get_letters.__name__)
