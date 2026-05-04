a = ("OnePlus","Nokia","Redmi")
print("Before Conversion",type(a))

a = list(a)
print("after conversion", type(a))
a.append("Vivo")
print(a)
a= tuple(a)
print(type(a))
print(a)

print(a.count("Redmi")) #gives the number of occurence of the value

print(a.index("Redmi")) #Gives the index number of the Element
