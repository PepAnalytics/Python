import time
class TrafficLight:

    __color = 'white'

    def running(self):
      while True:
          print('Red')
          time.sleep(7)
          print('Yellow')
          time.sleep(2)
          print('Green')
          time.sleep(10)



pep = TrafficLight()
pep.running()