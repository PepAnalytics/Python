# 5е задание
import random


# my_sps = []
# # for i in range(100, 1000, 2):
# #     my_sps.append(i)
# #
# # print(my_sps)
#
# #
#
from functools import reduce

my_sps = []

def numbers_sum(first, last):
    for i in range(100, 1000, 2):
        my_sps.append(i)
    return first + last


result = reduce(numbers_sum, my_sps)
print(result)
