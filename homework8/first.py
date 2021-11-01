class Data:

    def __init__(self, date_time):
        self.date_time = str(date_time)

    @classmethod
    def integer(cls, date_time):
        newlist = [ ]
        for i in date_time.split('.'):
            i = int(i)
            newlist.append(i)
        return newlist

    @staticmethod
    def validate(date_time):
        new_favorite = [ ]

        for i in map(int, date_time.split('.')):
            if 1 <= i <= 31:
                new_favorite.append(i)
                if 1 <= i <= 12:
                    new_favorite.append(i)
                    if 1 <= i <= 2020:
                        new_favorite.append(i)
                        return f'All is right'
                    else:
                        return f'Corrected your year'
                else:
                    return f'Corrected your month'
            else:
                return f'Corrected your day'

        print(new_favorite)

    def __str__(self):
        return self.date_time


# a = Data('23.11.2011')
# print(a)
print(Data.validate("10.12.1197"))
print(Data.integer("10.12.1197"))
