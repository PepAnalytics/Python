# первое задание
def zp():
    hour_pay = ''
    hour = ''
    prize = ''
    payment = input(f'enter number: {hour + hour_pay + prize}')
    new_payment = payment.split(' ')
    while True:
        hour = int (new_payment [ 0 ])
        hour_pay = int (new_payment [ 1 ])
        prize = int (new_payment [ 2 ])
        result = hour * hour_pay + prize
        break

    print(result)


zp()
