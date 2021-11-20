def fibonacci():
    x = 0
    yield x

    y = 1
    yield y

    while True:
        yield x + y
        x, y = y, x + y

generator = fibonacci()
for i in range(1):
    print(next(generator))
