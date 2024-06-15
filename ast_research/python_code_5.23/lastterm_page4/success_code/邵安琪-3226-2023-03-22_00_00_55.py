def search(x):
    n = len(x)    
    for a in x:
        if x.count(a)>n//2:
            b = a
        else:
            b = "False"
    return b
    






nums = eval(input())
y = search(nums)
print(y)


