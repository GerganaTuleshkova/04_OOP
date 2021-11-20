class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.keys = list(self.dict_obj.keys())
        self.current_key = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_key == len(self.dict_obj):
            raise StopIteration

        key_index_to_take = self.current_key
        self.current_key += 1
        return (self.keys[key_index_to_take], self.dict_obj[self.keys[key_index_to_take]])

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
