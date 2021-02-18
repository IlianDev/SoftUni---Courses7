import sys
n_snowballs = int(input())

max_snowball_value = - sys.maxsize
max_snowball_time = - sys.maxsize
max_snowball_quality = - sys.maxsize
max_snowball_snow = - sys.maxsize

for _ in range(n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if max_snowball_value < snowball_value:
        max_snowball_value = snowball_value
        max_snowball_time = snowball_time
        max_snowball_snow = snowball_snow
        max_snowball_quality = snowball_quality
print(f'{max_snowball_snow} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})')

