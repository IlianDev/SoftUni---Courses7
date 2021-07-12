class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Invalid age")
        return age

    def break_time(self):
        return "Resting..."


class Employee(Person):
    def __init__(self, name, age, data):
        super().__init__(name, age)
        self.data = data


class Manager(Person):
    def __init__(self, name, age, people_managing):
        super().__init__(name, age)
        self.people_managing = people_managing


class Contractor(Person):
    def __init__(self, name, age, date_of_expiry):
        super().__init__(name, age)
        self.date_of_expiry = date_of_expiry


class HR(Person):
    def __init__(self, name, age, emp_people):
        Person.__init__(self, name, age)
        self.emp_people = emp_people


e = Employee("test_E", 40, "20.02")
print(e.name, e.age, e.data)

m = Manager("Test_M", 35, 5)
print(m.break_time())

c = Contractor("test_C", -5, "20.04")
print(c.name, c.age)
