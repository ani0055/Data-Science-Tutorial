A = ["Ross", "Rachel", "Monica", "Joe"]


#program to swap 1st and 4th element
A[0],A[3]=A[3],A[0]
print(A)

#Program to add a new  value at 2nd position
A.insert(1,"Chandler")
print(A)

#Delete from 3rd position
A.pop(2)
print(A)

B= [13,7,12,10]
#program to multiply all the elements of the list
M = 1
for i in B:
    M = M*i

print(M)

#program to get the largest number in the list
B.sort()
print(B[-1])
#Smallest value in list
print(B[0])
















