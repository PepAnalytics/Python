class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'We started fo it {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'This picture drowing with Pen {self.title}'


class Pencel(Stationary):
    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'This picture drowing with Pencel {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'This picture drowing with Handle {self.title}'


now = Stationary

now.draw(Pen)
