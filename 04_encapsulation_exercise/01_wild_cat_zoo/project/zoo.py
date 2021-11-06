class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == 0:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        self.__animal_capacity -= 1
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker_obj in self.workers:
            if worker_obj.name == worker_name:
                self.workers.remove(worker_obj)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = 0
        for worker_obj in self.workers:
            all_salaries += worker_obj.salary

        if all_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= all_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        all_caring_costs = 0
        for animal_obj in self.animals:
            all_caring_costs += animal_obj.money_for_care

        if all_caring_costs > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= all_caring_costs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_types_count = {
        "Lion": [],
        "Tiger": [],
        "Cheetah": []}
        resulting_string = f"You have {len(self.animals)} animals\n"

        for animal_obj in self.animals:
            animals_types_count[animal_obj.__class__.__name__].append(animal_obj)

        for animal_type, animals_list in animals_types_count.items():
            resulting_string += f"----- {len(animals_list)} {animal_type}s:\n"
            for animal in animals_list:
                resulting_string += f"{animal}\n"

        return resulting_string.strip()

    def workers_status(self):
        workers_types = {
            "Keeper": [],
            "Caretaker": [],
            "Vet": []
        }
        resulting_string = f"You have {len(self.workers)} workers\n"

        for worker_obj in self.workers:
            workers_types[worker_obj.__class__.__name__].append(worker_obj)

        for worker_type, workers_list in workers_types.items():
            resulting_string += f"----- {len(workers_list)} {worker_type}s:\n"
            for worker in workers_list:
                resulting_string += f"{worker}\n"

        return resulting_string.strip()