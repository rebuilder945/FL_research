def search(x):
    ls=[]
    lt=[]
    for i in range(len(x)):
        if x[i] in lt:
            continue
        lt.append(x[i])
        ls.append(x.count(x[i]))
    return x[ls.index(max(ls))]





nums = eval(input())
y = search(nums)
print(y)


