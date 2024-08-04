import sys
import dis

n1 = [0] * 3
n2  = [0,0,0]
n3 = [0 for _ in range(3)]

n1.append(1)
n2.append(2)

print(sys.getsizeof(n1))
print(sys.getsizeof(n2))
print(sys.getsizeof(n3))

n3.append(3)

dis.dis("[0]*3")
dis.dis("[0,0,0]")
dis.dis("[0 for _ in range(3)]")


