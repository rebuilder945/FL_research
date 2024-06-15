def search(x):
    n = len(x)    
    for a in range(x):
        if a>n//2:
            b = a
        else:
            b = "False"
    return b
    






nums = eval(input())
y = search(nums)
print(y)


