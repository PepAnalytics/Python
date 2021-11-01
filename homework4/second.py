def choice_number():
    numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [numbers[i] for i in range(1,len(numbers)) if numbers[i] > numbers[i - 1]]
    return result



print(choice_number())
