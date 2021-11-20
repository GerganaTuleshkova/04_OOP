class vowels:
    VOWELS = "AEIOUY"

    def __init__(self, given_string):
        self.given_string = given_string
        #self.vowels_only = [ch for ch in self.given_string if ch.upper() in self.VOWELS]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.given_string) and self.given_string[self.index].upper() not in self.VOWELS:
            self.index += 1

        if self.index == len(self.given_string):
            raise StopIteration

        current_index = self.index
        self.index += 1
        return self.given_string[current_index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


