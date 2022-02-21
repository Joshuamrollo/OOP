import random

class insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4

    def flight(self):
        length = random.randint(0, 10)
        print('your insect flew ' + str(length) + ' miles')


        