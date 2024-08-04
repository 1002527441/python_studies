f = lambda:"Hello world"
print(f"f()={f()}")

x= lambda a, b: a + b
print(f"a+b={x(3,5)}")


numbers1 = [1,2,3,4,5,6,7,8]
squard = list(map(lambda x:x**2, numbers1))
print(f"squard={squard}")

even_numbers  = list(filter(lambda x:x%2==0, numbers1))
print(f"even_number={even_numbers}")


from functools import reduce

product = reduce(lambda x,y:x*y, numbers1)

print(f"product={product}")