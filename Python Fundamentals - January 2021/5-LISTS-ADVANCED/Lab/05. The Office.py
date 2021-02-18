happines = [int(el) for el in input().split()]
# happiness = list(map(lambda el:int(el), input().split()))
factor = int(input())
multiplies_happiness_by_factor = [num * factor for num in happines]
# multiplies_happiness_by_factor = list(map(lambda num: num * factor, happiness))

avg_happiness = sum(multiplies_happiness_by_factor) / len(multiplies_happiness_by_factor)

# with for loop
# happy_employees = []
# for h in multiplies_happiness_by_factor:
#     if h >= avg_happiness:
#         happy_employees.append(h)

happy_employees = [h for h in multiplies_happiness_by_factor if h >= avg_happiness]

# with filter
#happy_employees = list(filter(lambda h: h > avg_happiness, multiplies_happiness_by_factor))

half_n = len(multiplies_happiness_by_factor) / 2
if len(happy_employees) >= half_n:
    print(f"Score: {len(happy_employees)}/{len(multiplies_happiness_by_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplies_happiness_by_factor)}. Employees are not happy!")