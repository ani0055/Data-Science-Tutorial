# function to find maximum of three numbers
def max(a, b, c):
    if a>b and a>c:
        print(a,"is greatest")
    elif b > c and b > a:
        print(b , "is the greatest")
    else:
        print(c, "is the greatest")
max(16,25,37)

# Write a function to print and create a list of square of numbers between 1 to 30

def create_List():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l

print(create_List())

# Write a program that takes a number as a parameter and check if it is prime or not

def checkPrime(num):
    if(num == 1):
        print("Neither prime nor composite")
    if(num == 2):
        print("Is a prime number")
    else:
        for i in range(2,num):
            if num % i == 0:
                print(" it is not a prime number")
                break
        else:
            print("It is a prime number")

checkPrime(17)

# write a python function to sum all the numbers in a list
def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return total


print(add([16,21,38,49,51,66,71,84,96]))


# Write a python program to write the fibonaci sequence
def fib(num):
    if num == 1 :
        return 0
    elif num ==2:
        return 1
    return fib(num-1)+fib(num-2)
print(fib(8))


