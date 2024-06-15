def search(n):
    ls=[]
    for x in n:
        a=n.count(x)
        ls.append(a)
    b=max(ls)
    c=ls.index(b)
    d=n[c]
    if b>=float(len(n)/2):
        return d
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


