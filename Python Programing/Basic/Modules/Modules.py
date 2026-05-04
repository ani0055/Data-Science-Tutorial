# Modules are the .py files that contains set of functions you want to include in your program

# Built-in Modules
# Datetime Module:
import datetime as dt

x = dt.datetime.now()
print(x)

y = dt.datetime(1997,10,14)
print(y.strftime("%A"))


# random Module

import random as rd
l = ["Heads", "Tails", "heads", "tails"]
x = rd.randint(1,100)
print(x)
y = rd.choice(l)
print(y)


# math module

import math
x = max(13,34,69)
print("The maximum value is", x)
y = min(13,24,2)
print(y)

a = pow(2,5)
print(a)

b = math.sqrt(52)
print(b)

c = abs(-12.56)
print(c)

k = math.ceil(12.4) # next closet number
print(k)

f = math.floor(12.9) # previous closest number
print(f)














