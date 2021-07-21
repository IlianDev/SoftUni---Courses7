class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.topping_capacity = toppings_capacity
        self.toppings = {}
        # toppings = {topping_type: topping_weight}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def topping_capacity(self):
        return self.__topping_capacity

    @topping_capacity.setter
    def topping_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__topping_capacity = value

    def add_topping(self, topping):
        if len(self.toppings) >= self.topping_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight

        for _, topping_weight in self.toppings.items():
            total_weight += topping_weight

        return total_weight
