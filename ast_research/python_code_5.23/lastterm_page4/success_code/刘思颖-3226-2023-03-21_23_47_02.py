def search(y):
    n=len(y)
    for i in y:
        if y.count(y)>n//2:
            z=i
        else:
            z=False
    return z





nums = eval(input())
y = search(nums)
print(y)


