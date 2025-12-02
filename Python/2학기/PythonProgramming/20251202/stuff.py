import os
import random

cake = ['Cheese', 'Peach']

def dice(m):
    return random.randint(1, m)

class oven:
    def __init__(self):
        self.time = 0
        self.temp = 0
    def settime(self, t):
        self.time = t
    def settemp(self, t):
        self.temp = t
    def bake(self):
        print("baking at Temp", self.temp)
        print("for", self.time, "minutes")
if __name__ == '__main__':
    # print('stuff.py', os.getcwd())
    t = oven()
    t.settime(5); t.settemp(200)
    t.bake()

    for i in range(50):
        print(dice(6), end = ' ')
    print()

print("stuff.py", __name__)