# Functions are a set of code, which once created they can be used throughout the program.
# Functions help break our program into smaller parts and helps it look more organized and manageable

# 2 Functions Defined(body) and called

def Base():
    print("hello world")

Base()

def add():
    x=2
    y=5
    print(x+y)

add()

# Passing the parameters in the function
def add(x,y):
    return x+y

# Return keyword kin python is used to exit a function and return the value of the function

a = add(69,81)
print(a)

def name(name):
    print("Hello my name is ", name)

name("Animesh")