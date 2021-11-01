def my_func():
    numbers = input("Enter the number: ")

    while True:
        new_numbers =sum(map(int, ' '.join(numbers).split()))
        print(new_numbers)
        numbers = input("Enter the number: ")
        while True:
            new_numbers_twice = sum(map(int, ' '.join(numbers).split()))
            new_numbers_new = new_numbers + new_numbers_twice
            print(new_numbers_new)
            break
            if False:
                print(new_numbers_new)
                break

        
my_func()