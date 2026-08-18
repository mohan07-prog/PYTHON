def count_freq(string, target):
    count=0
    for ch in string:
        if ch== target:
            count+=1
    return count

text=(input("Enter a string: "))
target=input("Enter the target: ")
res=count_freq(text,target)
print(res)