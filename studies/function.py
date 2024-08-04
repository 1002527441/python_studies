def max(a,b):
    if a>b:
        return a
    else:
        return b


def fib(n):
    if (n==1 or n==2):
        return n
    x = fib(n-1)+fib(n-2)
    print(f"n={x}")
    return x