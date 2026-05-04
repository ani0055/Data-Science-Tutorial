#continue statement is used when you want to skip a particular condition
#break statement is used when you want to destroy a loop at a certain condition and come out of the loop

for i in range (1,11):
    if i == 3 or i == 5 or i == 6 or i == 7:
        continue
    else:
        print(i)

for i in range (1,11):
    if i == 7:
        break 
    else:
        print(i)




















