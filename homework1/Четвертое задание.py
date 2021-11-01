while True:
    number = input('Enter the number: ')
    new_number = list(number)
    if int(number) <= 0:
        break
    print(max(new_number))
