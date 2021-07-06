def draw_rhombus(n):
    for i in range(n):
        offset = (n - i - 1) * " "
        content = ("* " * (i + 1)).strip()
        print(f"{offset}{content}")

    for i in range(n - 2, -1, -1):
        offset = (n - i - 1) * " "
        content = ("* " * (i + 1)).strip()
        print(f"{offset}{content}")


draw_rhombus(5)
draw_rhombus(4)
draw_rhombus(3)
draw_rhombus(2)
draw_rhombus(1)