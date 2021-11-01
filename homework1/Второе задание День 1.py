my_sec = int(input('Enter secunds: '))

hour = my_sec // 3600
minute = my_sec // 60 - hour*60
secund = my_sec % 60

print(f'{hour}: {minute}: {secund}')