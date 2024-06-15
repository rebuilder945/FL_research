def search(x):
    c=[]
    for i in x:
        a=x.count(i)
        if a>=i//2:
            c.append(i)
    if c==[]:
        return False
    else:
        return i





nums = eval(input())
y = search(nums)
print(y)


