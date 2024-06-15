def search(x):
    c=[]
    for i in x:
        a=x.count(i)
        if a>lens(x)//2:
            c.append(i)
    if c==[]:
        return False
    else:
        return c[0]





nums = eval(input())
y = search(nums)
print(y)


