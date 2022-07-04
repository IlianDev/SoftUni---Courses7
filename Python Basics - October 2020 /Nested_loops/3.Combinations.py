n = int(input())
counter = 0
for f_number in range(0, n+1):
    for s_number in range(0, n+1):
        for t_number in range(0, n+1):
            if f_number+s_number+t_number == n:
                counter += 1
print(counter)