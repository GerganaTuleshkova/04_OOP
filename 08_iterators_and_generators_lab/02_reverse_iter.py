class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable_obj = list(iterable_obj)
        self.index = len(self.iterable_obj)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        current_index = self.index
        self.index -= 1
        return self.iterable_obj[current_index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

