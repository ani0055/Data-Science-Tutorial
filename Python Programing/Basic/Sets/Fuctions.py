#add
a = {"Ironman","Hulk","Thor","Captain America","SpiderMan"}
a.add("Dr. Strange")
print(a)

#pop (Randomly removes any item)
a.pop()
print(a)

#Remove
a.remove("Hulk")
print(a)

#Copy
b = a.copy()
print(b)


a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman","Flash","AquaMan"}
c = {"Hulk","Thor","Spiderman"}

#isdisjoint
print(a.isdisjoint(b))

#issubset
print(a.issubset(b))

#issuperset
print(a.issuperset(c))

#update
a.update(b)
print(a)

#Clear
a.clear()
print(a)


a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman","Flash","AquaMan"}
c = {"Hulk","Thor","Spiderman"}

#Union
print(a.union(c))

#Difference
print(a.difference(c))

#Difference Update
# a.difference_update(c)
# print(a)

#Intersection
x = (a.intersection(c))
print(x)

#Symentic difference
#The symmetric difference of two sets, denoted as $ A \Delta B $, is the set of elements that are in either set $ A $ or set $ B $, but not in their intersection.

x = a.symmetric_difference(c)
print(x)
