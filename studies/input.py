import os


#name = input("please enter your name:")
#print("Hello "+name)

x  = os.getcwd()

print(x)

f  = open("list.py","r")
print("filename:"+f.name)
print("Closed:"+ str(f.closed))
str1 = f.readlines()
print(str1)


