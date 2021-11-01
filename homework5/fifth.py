# with open ('5th_homew.txt','w') as firth:
#     firth.write('2 3 4 5 6 7')


with open('fivedaystask.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_numb = line.split()

        print(sum(map(int, my_numb)))



