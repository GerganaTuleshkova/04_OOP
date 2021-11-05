class Profile:
    min_username_len = 8
    max_username_len = 15
    min_password_len = 8

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < self.min_username_len or len(value) > self.max_username_len:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return f"{'*' * len(self.__password)}"

    @password.setter
    def password(self, value):
        self.check_password(value)
        self.__password = value

    def check_password(self, new_password):
        error_message = f"The password must be {self.min_password_len} " \
                        f"or more characters with at least 1 digit and 1 uppercase letter."
        if len(new_password) < self.min_password_len:
            raise ValueError(error_message)
        if not any([ch for ch in new_password if ch.isupper()]):
            raise ValueError(error_message)
        if not any([ch for ch in new_password if ch.isdigit()]):
            raise ValueError(error_message)

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'


#profile_with_invalid_password = Profile('My_username', 'My-password')
#profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
