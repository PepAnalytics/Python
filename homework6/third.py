class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.postition = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name}, {self.surname}'

    def get_total_income(self):
        a = sum(self._income.values())
        return a


info = Position('Parviz','Mammadov','Data Analytic',120000,30000)

print(info.get_full_name())
print(info.get_total_income())