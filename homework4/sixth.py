from itertools import cycle
c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c = c + 1


import itertools

progr_lang = [ "python", "java", "perl", "javascript" ]
iter = itertools.cycle(progr_lang)

for i in progr_lang:
    print(next(iter))
    if False:
        break
