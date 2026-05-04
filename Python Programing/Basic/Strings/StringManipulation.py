# 10 methods on string
from itertools import count

a = "Hi my name is Animesh Gawhale"

#length
print(len(a))

#Number of Caracters
print(a.count("a"))

#Converting the String into A upperCase
print(a.upper())

#Converting The string into lower case
print(a.lower())

#In title form ist letter of the word will be capital
print(a.title())

#For printing index number of a element
print(a.index("is"))

#for printing The string in the center center(no. of total letters, symbol)

print(a.center(100,'*'))

#str.center(width, fillchar) returns a centered string of length width, padded with fillchar on both sides.
x = "Rahul"
print(x.center(len(x)+8,"*")+"GDSS")















