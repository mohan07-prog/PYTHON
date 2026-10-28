numbers = [1,2,3,4,5]

def doubled(x):
    return x*2

double = list(map(doubled, numbers))
print(double)