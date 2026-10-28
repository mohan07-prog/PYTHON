from functools import reduce
numbers = [1,2,3,4,5]

def multiply(x,y):
    return x*y

num = reduce(multiply, numbers)
print(num)