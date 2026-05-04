#Strting Reversal
a = input("Give A string input : ")
print(a[::-1])

#Write a program to check if every word in a string contains only digits
b = a.isdigit()
if b==True:
    print("String Contains only digits")
else:
    print("String does not contain only digits")

if a == a[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

vowels = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o"  or  i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels += 1

print("Vowels in the String is : ", vowels)

# Write a program to check if every word in the string begins with capital letter

print(a.istitle())


















