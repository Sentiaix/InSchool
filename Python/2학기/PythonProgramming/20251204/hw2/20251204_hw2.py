from car import bmw
import mydevice

fast = bmw(325, 4)
fast.gas()
fast.gas(12)
print(fast.speed())
fast.cbreak(1)
fast.cbreak(2)
print(fast.speed())

if mydevice.speedgun(fast) > 30 :
    print('speeding ticket')
else:
    print('no speed ticket')