from project_people.person import Person
from project_people.employee import Employee


class Teacher(Person, Employee):
    def teach(self) -> str:
        return "teaching..."


t = Teacher()
print(t.sleep())
print(t.get_fired())
print(t.teach())
