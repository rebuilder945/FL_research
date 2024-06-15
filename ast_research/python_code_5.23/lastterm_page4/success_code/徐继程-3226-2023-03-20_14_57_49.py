def search(n):
    ls=[]
    if x in n:
        a=n.count(x)
        ls.append(a)
    b=max(ls)
    c=n.index(ls)
    d=n[c]
    return d






nums = eval(input())
y = search(nums)
print(y)


