from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    _dvd_capacity = 15
    _customer_capacity = 10
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls._dvd_capacity

    @classmethod
    def customer_capacity(cls):
        return cls._customer_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) == self._customer_capacity:
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) == self._dvd_capacity:
            return
        self.dvds.append(dvd)

    def get_customer_from_id(self, customer_id: int):
        for customer_obj in self.customers:
            if customer_obj.id == customer_id:
                return customer_obj

    def get_dvd_from_id(self, dvd_id: int):
        for dvd_obj in self.dvds:
            if dvd_obj.id == dvd_id:
                return dvd_obj

    def rent_dvd(self, customer_id: int, dvd_id: int):
        if self.get_customer_from_id(customer_id) and self.get_dvd_from_id(dvd_id):
            customer = self.get_customer_from_id(customer_id)
            dvd = self.get_dvd_from_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        if self.get_customer_from_id(customer_id) and self.get_dvd_from_id(dvd_id):
            customer = self.get_customer_from_id(customer_id)
            dvd = self.get_dvd_from_id(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        resulting_string = "\n".join([str(c) for c in self.customers]) + "\n"
        resulting_string += "\n".join([str(d) for d in self.dvds])
        return resulting_string




