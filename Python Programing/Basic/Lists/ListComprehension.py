L1 = [30,40,50,60]
L2 = []
L3 = [i for i in L1 if i>=40] # List Comprehension

for i in L1:
    if i>45:
        L2.append(i)

print(L1,"\n",L2)
print(L3)




































