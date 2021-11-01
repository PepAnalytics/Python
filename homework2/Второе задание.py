my_new_list = input('Введите что-то: ').split()
print(my_new_list)


for i in range(0, len(my_new_list)-1, 2):
    my_new_list[i], my_new_list[i + 1] = my_new_list[i + 1], my_new_list[i]

print(my_new_list)