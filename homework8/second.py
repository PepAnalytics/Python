class Check:

    def __init__(self,number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def my_func(number_1,number_2):
        try:
            result = number_1 / number_2
            return result
        except ZeroDivisionError:
            print('You cannot divide by zero')







print(Check.my_func(13,0))