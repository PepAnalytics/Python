# with open('info.txt', 'w') as new:
#     new.write('Mamedov:' '26000\n')
#     new.write('Karpov:' '16000\n')
#     new.write('Ponamorenko:' '21000\n')
#     new.write('Yevtuwenko:' '47000\n')


with open('info.txt') as info:
    my_dict = {line.split(':')[0]: int(line.split(':')[1]) for line in info}
    average = (print(f'average : {sum(my_dict.values()) / len(my_dict)}'))
    less_than = {print (f'{keys}: {values}') for keys, values in my_dict.items() if values < 20000}
