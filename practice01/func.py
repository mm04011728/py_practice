def add(x, y, f):
    return f(x) + f(y)


def abs(num):
    if num >= 0:
        return num
    else:
        return -num


def power_2(num):
    return num*num

def num(num):
    return num

sum = add(-5, 3, abs)
print(sum)
sum = add(3, -8, power_2)
print(sum)

sum = add(3,3,lambda x:x)
print(sum)