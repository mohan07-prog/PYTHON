numbers = [1,2,3,4,5,6,7,8,9,10,22,22,23,45,66,43,89,67,64,86]

def even(x):
    return x%2 == 0

num = list(filter(even, numbers))
print(num)