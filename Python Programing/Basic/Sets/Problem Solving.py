# Program to print maximum and minimum value in the set
a = {12,21,95,25,78,6,66,2,89}
max =max(a)
min =min(a)
print("Maximum value in the set is ",max)
print("Minimum value in the set is ",min)

# Program to find the common elements in the three list using set
a = [1,34,69,20,71]
b = [69, 84, 20, 98, 71]
c = [71,84,20,34,11,65]

print("Common elements in the three sets are: ", set(a) & set(b) & set(c))

a = {1,5,8,9,16,27,61}
a.discard(61) # removes the given element from the set
print(a)












