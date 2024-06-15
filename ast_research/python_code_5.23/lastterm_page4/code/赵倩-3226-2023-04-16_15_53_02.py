def search(x1):
    x2 = 0
    for x in x1:
        if x1.count(x)>len(x1)/2:
            x2 = x
    if x2!=0:
        return x2
    elif x2==0:
        return 'False'def search(x1):
    x2 = 0
    for x in x1:
        if x1.count(x)>len(x1)/2:
            x2 = x
    if x2!=0:
        return x2
    elif x2==0:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


