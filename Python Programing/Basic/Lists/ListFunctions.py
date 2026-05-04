a = ["Ironman", "Thor","Hulk","Captain America","Hulk"]
print(len(a))
print(a.count("Hulk"))#To count the occurence of the particular element

a.append("Spiderman")#to add an element at the end of list
print(a)

a.insert(2,"Vision")#Insertiong element at the particular inmdex
print(a)

a.remove("Hulk")#to remove ethe 1st appearence of the element
print(a)

print(a.pop(2))# to remove the value at a certain index
print(a)

b = a.copy() #to copy a list
print(b)

print(a.index("Ironman"))#to get the value of index of element

c = ["Dr. Strange", "Vision", "Black Widow"]
a.extend(c) #to extend the list with a new list at the end
print(a)

a.reverse()#Reverse a List
print(a)

a.sort()#FOR SORTING THE list in assending order
print(a)

#to clear all the data from the list
c.clear()
print(c)












