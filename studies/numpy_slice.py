import numpy as np

print("a slice with slice()")
a = np.arange(10,dtype=int)
print(a)

s  = slice(2,9,2)
print(a[s])

print("using ...")
b = np.array([[1,2,3],[4,5,6],[6,7,8]])
print(b)
print(b[...,0])
print(b[1,...])
print(b[...,1:])

print("advance.... slice")
x = np.array([[1,2],[3,4],[5,6]])
print(x)
y = x[[0,1,2],[0,0,1]]
print(y)
