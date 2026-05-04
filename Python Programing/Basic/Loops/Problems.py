# 1st Question
# sum = 0
# for i in range (0,51):
#     if i%2==0:
#         sum += i
#
# print(sum)

# 2nd Question

# for i in range (1,21):
#     print(i," : ",i**2)
#


# 3rd Question

# sum = 0
# n=0
# while n <=20 :
#     if n%2 != 0:
#         sum += n
#     n += 1
#
#
#
# print(sum)


#4th Question
# for i in range(1,101):
#     if i%8==0 and i%12 == 0:
#         print(i)


#5th Question
# BIlling system

while True:
    name = input("Enter Customer name : ")
    total = 0

    while True:
        print("Enter the amount and Quaintity")
        amount = float(input("Enter The Amount : "))
        quantity = float(input("Enter the quantity : "))
        total += amount*quantity
        repeat = input("Do you want to add more Items? (Yes/No) : ")

        if repeat == "no" or repeat == "No" or repeat == "N":
            break

    print("-"*40)
    print("Name : ", name)
    print("Amount to be paid : ",total)
    print("-"*40)
    print("********** Happy Shopping ***********")

    repeat1 = input("If you want to go to next customer (Yes/No) : ")
    if repeat1 == "No" or repeat == "no":
        break













