a = ("Oneplus","Vivo","Redmi","Samsung","Nokia")

print(a[1:3])#top get elements in this range
print(a[:3])#To get elements from 0 to 2
print(a[2:])#to get elements from 2 to end
print(a[::2])#printing with a gap of 2
print(a[::-1])



#with for loop

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

#Along with While Loop

i= 0
while i<len(a):
    print(a[i])
    i+=1

















