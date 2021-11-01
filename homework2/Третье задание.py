number = int(input('Enter the number of month: '))

month = {
    1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
    7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'
}

print(month.get(number))

month = ['1: winter',  '2: winter',  '3: spring', '4: spring', '5: spring', '6: summer',
   ' 7: summer', '8: summer', '9: autumn', '10: autumn', '11: autumn',  '12: winter']

print(month[number-1])
