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

'''
Tова е общото, повтарят се: 
self.name = name
self.age = age

слагаме в скобите, класа Person, чйито проперти искаме да бъдат видяни 
class Employee(Person):
    def __init__(self, name, age, data):
        super().__init__(name, age)     --> супер и пожтарящия с екод
        self.data = data
        
валидация на години
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Invalid age")
        return age
    
    ---> можем да добажим инит метод на персон рестинг които пак ще се наследи от вс класове по надолу
    и при нужда можем да го ползваме 
        def break_time(self):
        return "Resting..."
        
--> ако наследява парент клас даден клас ако не сме дефинирали интин метод идето отива в парент класа гледа 
дали там има такъж метод и го изпълнява. 
'''
