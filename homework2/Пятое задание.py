# пятое задание

new_cell = int(input('Enter the number: '))
my_list = [ 7, 5, 3, 3, 2 ]

for i in range(len(my_list)):
    if new_cell >= i:
        my_list.insert(i,new_cell)
        my_list.sort()
        my_list.reverse()
        break

print(my_list)
