#write a program to get fibonacci series upto 10 numbers
# a = 0
# b = 1
# sum = 0
# print(a)
# print(b)
#
# for i in range (2,11):
#     c= a+b
#     a = b
#     b = c
#
#     print(c)

# to check if a number ius prime or not
# n = int(input("Enter the Number : "))
# if n<=1:
#     print("Neither Prime nor Composite")
#
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("Number is not a prime Number")
#             break
#     else:
#         print("Number is a Prime Number")


#To check if the number is palindrome or not
# n = int(input("Enter the Number to Check : "))
# temp = n
# rev = 0
# while(n>0):
#     dig = n%10
#     rev = rev*10+dig
#     n = n//10
#
# if temp == rev:
#     print("Number is a Palindrome")
# else:
#     print("Number is not palindrome")
#
print("********** Area Calculator **********")
print("""Press 1 to get the area of the Square.
Press 2 to get the area of the Rectangle.
Press 3 to get the area of the Circle.
Press 4 to get the area of the Triangle.""")

choice = int(input("Enter Your Choice : "))

if choice == 1:
    side = float(input("Enter the Side of Square : "))
    Area = side*side
    print("Area of Square : ",Area)

elif choice == 2:
    Length = float(input("Enter the Length of Rectangle : "))
    Breadth = float(input("Enter the Breadth of Rectangle : "))
    Area = Length* Breadth
    print("Area of Rectangle : ",Area)

elif choice == 3:

    Radius = float(input("Enter the Radius of the circle : "))
    Area = (22/7)*Radius**2
    print("Area of the Triangle : ",Area)

elif choice == 4:
    Height = float(input("Enter the Height of the Triangle : "))
    Base = float(input("Enter the Base of the Triangle : "))
    Area = 0.5*Height*Base
    print("Area of the Circle : ",Area)

else:
    print("Enter a valid Choice")




























































































