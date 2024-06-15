def search(nums):
    a=list(nums)
    c=[]
    for x in a:
        b=a.count(x)
        c.append(b)
        e=max(c)
    return e






nums = eval(input())
y = search(nums)
print(y)


