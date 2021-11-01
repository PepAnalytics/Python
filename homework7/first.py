a = [[3, 5, 3], [2, 3, 5], [8, 3, 37]]
b = [[43, 2, 4], [6, 8, 3], [7, 1, 51]]

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return f'{self.my_list}'


    def __add__(self, other):
        c = []
        for i in range(len(self.my_list)):
            c.append([])
            for d in range(len(self.my_list[0])):
                c[i].append(self.my_list[i][d] + other.my_list[i][d])
            return ''.join(map(str, c))



c = Matrix(a)
print(c)

o = Matrix(b)
print(o)

print(c + o)
