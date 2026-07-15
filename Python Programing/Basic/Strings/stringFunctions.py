#endswith() - Returns true value if the strings end with the specified value
a = " Animesh Gawhale "
print(a.endswith("e"))

#startswith() - Returns true value if the strings starts with the specified value
print(a.startswith("AN"))

#Swapcase() - Swaps cases, lower to upper and upper to lower
print(a.swapcase())

#strip - returns a trimmed version of the string
print(a)
print(a.strip())#we can customize it

#split() - splits the string at the specified seprator, and returns a list
b = "#OOFD#BRB#OMW#TB"
print(b.split("#"))

#ljust() - returns a left justified versions of the string


x = a.ljust(50,"*")

print(x , " is my favorite movie")


#rjust() - returns a rigth justified versions of the string
# same as ljust from right side

#replace() - returns a string where a specified value is replaced with a specified value

print(a.replace("Animesh","Rajesh"))#for everywhere the old string is used


#rindex() - Searches the strings for a specified value and returns the last of where it was found

c ="He was a good boy until he had gone rouge against the church"
print(c.rindex("boy"))
print(c.rfind("against"))

















