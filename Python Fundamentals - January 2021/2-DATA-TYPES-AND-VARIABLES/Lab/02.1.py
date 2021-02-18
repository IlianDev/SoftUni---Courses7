import math
centuries = int(input())
years = centuries * 100
days = math.trunc(years * 365.2422)  # smqta si go obache ne otrazqwa nishto sled des zapetaq
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

