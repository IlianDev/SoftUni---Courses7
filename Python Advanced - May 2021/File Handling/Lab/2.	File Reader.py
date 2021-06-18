file = open("numbers.txt")

sum_nums = 0
for line in file:
    line = int(line)
    sum_nums += line
print(sum_nums)
