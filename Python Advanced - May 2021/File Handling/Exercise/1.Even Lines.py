# правя фунция, която да взима някой ред
import re


def replace_symbols(line):
    # смени тези неща за @ za liniqta koqto sme dali
    return re.sub(r"[-,\.\!\?]", "@", line)


with open("1.input_file.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(len(lines)):
        if row_number % 2 == 0:
            replaced = replace_symbols(lines[row_number]).split()
            print(' '.join(replaced[::-1]))
