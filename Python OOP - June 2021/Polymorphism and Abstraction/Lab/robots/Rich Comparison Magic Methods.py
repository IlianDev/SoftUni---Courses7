class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):  # може и така да се напише
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age


person_1 = Person("Test", 30)
person_2 = Person("Test2", 10)

print(person_1 < person_2)  # TRUE
