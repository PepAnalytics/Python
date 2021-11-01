with open(input('Файл: '),'w') as trr:
    while True:
        s = input()
        if s == '':
            break
        trr.write(s+'\n')
