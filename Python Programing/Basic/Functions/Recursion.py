# Recursion is most commonly used mathematical and programming
# In simple words recursion means a function can call itself giving us a benefit of looping through data in order to get a result

def factorial(N):
    if N == 0 or N==1 :
        return 1
    else:
        return N*factorial(N-1)


print(factorial(9))






