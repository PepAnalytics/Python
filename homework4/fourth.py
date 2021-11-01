from random import randint


my_list = [randint(1,40) for i in range(40)]
b = list(i for i in my_list if my_list.count(i)==1)
print(b)