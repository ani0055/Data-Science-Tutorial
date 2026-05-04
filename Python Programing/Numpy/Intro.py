# NumPy is the short form of Numerical Python.
# In 2005, Travis Oliphant created NumPy package
# Numpy is a package that defines multi dimensional array and associates fast math functions

# Arrays
# an array is defined as a collection of items that are stored at contiguous memory locations
# It is an container which can hold a fixed nimber of items, and these items should be of the same type
# A combination of arrays saves a lot of time

import numpy as np
l1 = [20,30,40]
l2 = [23,56,48]

print(l1+l2)

a = np.array([10,20,30])
b = np.array([40,50,60])
c = 16
print(a)
print(b)
print(a+b)
print(a*b)
print(c*a)

# Arrays vs. Lists
# A list cannot directly handle mathematical operations while array can
# An Array consumes ledd memory than a list
# Using an Array is faster than list
# A list can store different datatypes , while array can't do that
# A list is easier to modify since a list store each element individually it is easier to ass and delete an element than an array does
# In list you can have nisted data with different size, while you cannot do the same in array














