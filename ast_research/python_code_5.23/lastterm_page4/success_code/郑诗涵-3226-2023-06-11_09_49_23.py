def search(x):
    for i in x:
        n=len(x)
        a=n//2
        if (x.count(i))>(n//2):
            return i
        else:
            return False






nums = eval(input())
y = search(nums)
print(y)


