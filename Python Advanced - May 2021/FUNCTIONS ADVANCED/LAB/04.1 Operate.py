from functools import reduce


def operate(operator, *args):
    # eval() - означава еволюирай стринга като код,
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


print(operate("+", 1, 2, 3))
print(operate("-", 3, 4))
print(operate("*", 3, 4))
print(operate("/", 3, 4))
