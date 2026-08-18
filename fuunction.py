def check_even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
n=int(input("Enter The Number: ")) 
result=check_even_odd(n)
print(result)

list=(2,3,4,5,6,7,8,9,11)
for i in list:
    res= check_even_odd(i)
    print(res)