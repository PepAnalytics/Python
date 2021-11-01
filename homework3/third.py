def my_func(num1,num2,num3):
    my_list = [num1, num2, num3]
    my_list.remove(min(my_list))
    print(sum(my_list))



my_func(1,2,3)