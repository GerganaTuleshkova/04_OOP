class Checker:
    @classmethod
    def check_string(cls, value, error_message="Name cannot be empty string or white space!"):
        if value.strip() == "":
            raise ValueError(error_message)
        return value

    @classmethod
    def check_number(cls, value, error_message):
        if value <= 0:
            raise ValueError(error_message)
        return value