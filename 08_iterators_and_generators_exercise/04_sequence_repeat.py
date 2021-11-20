class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = 0
        self.iterations = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations > self.number:
            raise StopIteration

        current_index = self.current_index % len(self.sequence)
        self.current_index += 1
        self.iterations += 1
        return self.sequence[current_index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')


