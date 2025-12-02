# 20251202(Tue) <Module>

import os
import stuff
import stuff as s
from stuff import dice, cake, oven

k = oven()
k.settime(100)
k.bake()

print(os.getcwd())
print(stuff.cake)
print(stuff.dice(20))
for i in range(5): #cheese or peach random
    print(cake[dice(2)-1], end = ' ')
print(s.cake)