def int_func():
    word = input('Enter your word: ')
    while True:
        if word.islower():
            new_word = word.title()
            print(new_word)
            break


int_func()