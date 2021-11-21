class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.number = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 0:
            raise StopIteration

        current_number = self.number
        self.number -= 1
        return current_number


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
