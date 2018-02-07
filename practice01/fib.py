# 1 1 2 3 5 8 13 21....


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(15))
