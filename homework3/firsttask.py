
def first_func():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the first number: '))
    if b == 0:
        print('Can not entered zero!')
        pass
    elif b != 0:
        result = a / b
        print(result)
        return result


first_func()

