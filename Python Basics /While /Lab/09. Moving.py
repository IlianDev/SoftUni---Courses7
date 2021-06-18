width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height  # намираме обема които е равен на броя на кутиите, свободното място
command = input()  # имаме команда, която може да бъде или брой пренесени кашони или текстът "Done"
# спираме пренасянето ако командата стане равна на  Done
# продължаваме да се пренасяме ако командата е различна от   "Done'

while command != "Done":
    boxes = int(command)  # boxes от текст го правим на число и като местим кутиите в апартамента мястото там намалява
    free_space -= boxes
    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{free_space} Cubic meters left.")
