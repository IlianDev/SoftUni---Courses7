start_hour = int(input())
start_minutes = int(input())

total_in_minutes = start_hour*60 + start_minutes + 15
#za da smetna vs v minuti

final_hour = total_in_minutes // 60
# prevyrnah cqloto v chasove bez ostatyk
final_minutes = total_in_minutes % 60
#za da prevyrna cqloto vreme v minuti trqbva da % 60

if final_hour > 23:
    final_hour -=24

if final_minutes < 10:
    print(f"{final_hour}:0{final_minutes}")
else:
    print(f"{final_hour}:{final_minutes}")