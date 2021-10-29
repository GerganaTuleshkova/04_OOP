class Smartphone(object):
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def install(self, app, app_memory):
        if app_memory > self.memory:
            return f"Not enough memory to install {app}"

        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

    def power(self):
        self.is_on = not self.is_on


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
