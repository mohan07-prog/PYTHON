def count_freq(string):
    count=0
    for ch in string:
        if ch== "a":
            count+=1
    return count

text=(input("Enter a string: "))
res=count_freq(text)
print(res)