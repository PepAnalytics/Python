# with open ('fourth_task.txt','w') as hm:
#     hm.write('One — 1\n')
#     hm.write('Two — 2\n')
#     hm.write('Three — 3\n')
#     hm.write('Four — 4')

#
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('fourth_task.txt','w') as few:
    with open('fourth_task.txt','r') as new:
        few.write(str(line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in new))


