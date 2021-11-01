class Car:

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        print(f'Car {self.name} is has {self.speed},{self.colour} colour', {self.is_police})

    def go(self):
        return f'{self.name} is going'

    def stop(self):
        return f'{self.name} is stop'

    def turn(self):
        return f'{self.name} not right turn'

    def show_speed(self):
        return f'{self.name} has speed {self.speed}'




class TownCar(Car):
    def __init__(self, speed, colour, name, is_police):
        Car.__init__(self,speed,colour,name,is_police)

    def show_speed(self):
        # print(f'{self.name} has speed {self.speed}')
        if self.speed > 60:
                print(f'{self.name} has speed {self.speed},pls reduce speed')

class SportCar(Car):
    def __init__(self, speed, colour, name, is_police):
        Car.__init__(self,speed,colour,name,is_police)

class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police):
        Car.__init__(self,speed,colour,name,is_police)

    def show_speed(self):
        print(f'{self.name} has speed {self.speed}')
        if self.speed > 40:
                print(f'{self.name} has speed {self.speed},pls reduce speed')


class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police):
        Car.__init__(self,speed,colour,name,is_police)



my_car = TownCar(70,'red','Mers', True)

my_car.show_speed()