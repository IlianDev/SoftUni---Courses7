import math
income = float(input())
average_success = float(input())
minimal_salary = float(input())

social_sc = 0.35 * minimal_salary
excellent_sc = average_success * 25

# успех над 5.50 включително
    # Коя е по високата степендия ако уchенитък има право да получи и двете
# успех над 4.50 и по малко от 5.50
    # дох по малък от мин заплата
    # nqma pravo na stipendiq
# uspeh po malyk ili rawen na 4.50:
    # nqma pravo na stipendiq

if average_success >= 5.50:
    if income < minimal_salary:
        if excellent_sc >= social_sc:
            print(f"You get a scholarship for excellent results {math.floor(excellent_sc)} BGN")
        else:
            print(f"You get a Social scholarship {math.floor(social_sc)} BGN")
    else:
        print(f"You get a scholarship for excellent results {math.floor(excellent_sc)} BGN")

elif average_success > 4.5:
    if income < minimal_salary:
        print(print(f"You get a Social scholarship {math.floor(social_sc)} BGN"))
    else:
        print(f"You cannot get a scholarship!")

elif average_success <= 4.5:
    print(f"You cannot get a scholarship!")









