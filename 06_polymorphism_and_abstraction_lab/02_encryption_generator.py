class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ""
        for ch in self.text:
            new_ord = ord(ch) + other
            if new_ord > 126:
                new_ord = new_ord - 126 + 32 - 1
            if new_ord < 32:
                new_ord = 127 - (32 - new_ord)
            result += chr(new_ord)
        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
