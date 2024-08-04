import numpy as np

a = np.array([[1,2,3],[4,5,6]]) 
print(a.shape)    


b = np.zeros(5,dtype=int)
print(b)


c = np.ones([2,3], dtype=int, order='c')
print(c)


d = np.array([
    [1,2,3],
    [4,5,6],
    [6,7,8]])

print(d)

e  = np.zeros_like(d)
print(e)

f  = np.arange(10,20,1)
print(f)

g = np.linspace(1,2,10)
print(g)