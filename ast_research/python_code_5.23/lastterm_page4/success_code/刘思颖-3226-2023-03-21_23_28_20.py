def search(y):
    z=0
    a= len(y)//2
    for i in y:
        if y.count(y)>a:
            z=i
        else:
            z=False
    return z





nums = eval(input())
y = search(nums)
print(y)


