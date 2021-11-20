def genrange(start: int, end: int):
    for n in range(start, end + 1):
        yield n


print(list(genrange(1, 10)))