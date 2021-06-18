maximum_bad_grades = int(input())  # лошите оценки максимума който може да си позволи
total_score = 0  # общия им успех
number_of_problems = 0  # броя на проблемите. т.е колко пъти се е справил
last_problem = ""  # последния проблем
number_of_bad_grades = 0  # броя на лошите опити
too_many_bad_grades = False  # защото все още не е получил оценка затова е false
command = input()

while command != "Enough":  # ако е развно на enough цикъла ще проключи
    last_problem = command   # последния проблем му задавам да е равен на command, защото ако  command e enough цикълът
    # ще приключи
    current_grade = int(input())  # чета си какъв е успеха
    if current_grade <= 4:   # ako e по малък от 4
        number_of_bad_grades += 1  # увеличавам си броя на неуспешни опити
        if number_of_bad_grades == maximum_bad_grades:  # правя втора проверка ако броя неуспешни опити са равни на.
            # стават точно толкова колкото му е позволено
            # максималния броой си променям булевата на тру
            too_many_bad_grades = True  # за ориентир че е скъсан за лоши оценки и след това брейквам
            break  # има право на три лоши отговора издънил се е на изпита значи приключва
            # бреик ме праща директно на принтовете долу пропуска трите реда след бреик
    number_of_problems += 1
    total_score += current_grade
    command = input()  # чета изпит или  enough  защото изпита спира или когато срещне enough или последната задача

if too_many_bad_grades:
    print(f"You need a break, {number_of_bad_grades} poor grades.")
else:
    average_score = total_score / number_of_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
