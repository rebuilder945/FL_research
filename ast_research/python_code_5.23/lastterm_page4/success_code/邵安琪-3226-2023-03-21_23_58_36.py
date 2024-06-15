def search(x):
    for i in range(len(x)):
        a = x.count(x[i])
        if a>len(x)//2:
            b = a
        else:
            b = "False"
    return b
    






nums = eval(input())
y = search(nums)
print(y)


