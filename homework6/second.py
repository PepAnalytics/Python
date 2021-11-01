class Way:
    def __init__(self,length,weight):

        self._length = length
        self._weight = weight
    def result(self):
        my_res = self._length * self._weight * 25 * 5
        print(my_res)


my_way = Way(10,25)

my_way.result()

