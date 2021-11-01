
# with open ('second task','w') as sec:
#     sec.write('I want\n')
#     sec.write('learning\n')
#     sec.write('Big Date\n')


with open('second task') as sec:
    lines = 0
    words = 0

    for i in sec:
        dlinalista = i.split()
        lines = lines + 1
        words = words + len(dlinalista)
    print(words)
    print(lines)
