def check_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num=int(input("Enter the Number: "))
res=check_prime(num)
print(res)