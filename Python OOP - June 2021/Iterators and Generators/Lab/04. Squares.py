def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num ** 2
        current_num += 1


class squares:
    def __init__(self, end):
        self.end = end
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp ** 2


for el in squares(5):
    print(el)
