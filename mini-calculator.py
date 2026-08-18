def mini_calc(num1,num2,operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        return "invalid operation"
    
num1=int(input("Enter The Number 1: "))
num2=int(input("Enter The Number 2: "))
operation=input("Enter The Operation (+,-,*,/): ")
res=mini_calc(num1,num2,operation)
print("The Result: ",res)