from itertools import permutations


def possible_permutations(given_list):
    result = permutations(given_list)
    for i in result:
        yield list(i)


[print(n) for n in possible_permutations([1])]