
def new_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")
    firstname = (input('Enter the name: '))
    lastname = (input('Enter the lastname: '))
    email = (input('Enter the email: '))
    country = (input('Enter the country: '))
    age = (input('Enter your age: '))
    phone = (input('Enter the phone number: '))


    new_func(Firstname=firstname, Lastname=lastname, Email =email, Country=country, Age=age, Phone_number=phone)
    print(new_func())

new_func()

