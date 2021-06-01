n = int(input())

dict_students = {}

for x in range(n):
    student, degree = input().split()
    if student not in dict_students:
        dict_students[student] = []
    dict_students[student].append(float(degree))

for key, value in dict_students.items():
    print(f"{student} -> {value}")