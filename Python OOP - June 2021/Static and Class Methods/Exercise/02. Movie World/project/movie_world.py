from project.dvd import DVD
from project.customer import Customer

CONST_DVD_CAPACITY = 15
CONST_CUSTOMER_CAPACITY = 10


class MovieWorld:
    DVD_CAPACITY = CONST_DVD_CAPACITY
    CUSTOMER_CAPACITY = CONST_CUSTOMER_CAPACITY

    def __init__(self, name: str):
        self.name = str(name)
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity() -> int:
        # return MovieWorld.DVD_CAPACITY
        return __class__.DVD_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        # return MovieWorld.CUSTOMER_CAPACITY
        return __class__.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> bool:
        """add the customer if capacity not exceeded"""
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd: DVD) -> bool:
        """add the dvd if capacity not exceeded"""
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        # current_dvd: DVD = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
        current_dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]
        current_customer: Customer = list(filter(lambda c: c.id == dvd_id, self.customers))[0]

        if current_dvd.id in [d.id for d in current_customer.rented_dvds]:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        if current_dvd.is_rented:
            return f"DVD is already rented"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer: Customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd: DVD = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(repr(customer))
        for dvd in self.dvds:
            result.append(repr(dvd))
        return '\n'.join(result)

