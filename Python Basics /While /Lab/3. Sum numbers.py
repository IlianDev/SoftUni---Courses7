start_num = int(input())

sum_num = 0
# действие: взимаме число -> сумираме
# стоп : sum_numbers >= start_number
# продължава:  sum_numbers < start_number

while sum_num < start_num:
    number = int(input())  # dokato sum_numbers e po malko ot start_num procheti nqkakvo chislo i go sumirai
    sum_num += number

# ako sum_num >= start_num
else:
    print(sum_num)

