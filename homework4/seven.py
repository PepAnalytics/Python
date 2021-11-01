import math
import itertools



def my_fact():
    for numb in itertools.count(1):
        yield math.factorial(numb)


my_gen = my_fact()
a = 0

for i in my_gen:
    a += 1
    print(f'{a} factorial is: {i}')
    if a == 25:
        break
