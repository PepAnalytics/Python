
my_string = str(input('Enter the some text: '))
word_string = []
number_str = 1
for i in range(my_string.count(' ')+1):
    word_string = my_string.split(' ')
    number_str = i + 1
    if len(str(word_string)) > 10:
        print(word_string[i][0:10])
    else:

        print(number_str, word_string[i])
