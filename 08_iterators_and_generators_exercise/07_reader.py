def read_next(*args):
    iterables = list(args)
    index = 0

    while index < len(iterables):
        inner_index = 0
        for el in iterables[index]:
            yield el

        index += 1


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

