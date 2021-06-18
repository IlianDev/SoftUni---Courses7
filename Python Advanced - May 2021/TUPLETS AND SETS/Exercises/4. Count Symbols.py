text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)

sorted_data = sorted(symbols)
for el in sorted_data:
    print(f"{el}: {symbols[el]} time/s")

##връща лист от тюпъли, като използвам това сравнение с ламбда, което е мутабл
# sorted_data = sorted(symbols.items(), key=lambda x: x[0])
# for el in sorted_data:
#     print(f"{el[0]}: {el[1]} time/s")
