import math




t = ['a', 'b', 'c',  'd','e']
print(t[0:3])





names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.lower() for name in names if len(name)>2]
print(new_names)


multiples = [i for i in range(1,31) if i % 3 ==0]
print(multiples)



for n1 in names:
    if(len(n1)>3):
        print(n1.upper())

listdemo = ['Google', 'Runoob1', 'Taobaokill']
dict1 = {key.lower():len(key)*2 for key in listdemo}
print(dict1)


dic = {x:x**3 for x in (2,4,6,8,10) if x not in (4,10)}
print(dic)

#tuple
tu1=(x for x in range(1,10))
print(tuple(tu1))
