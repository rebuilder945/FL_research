def search(x):
    ls=[]
    lt=[]
    for i in range(len(x)):
        if x[i] in lt:
            continue
        lt.append(x[i])
        ls.append(x.count(x[i]))
    for s in range(len(ls)):
        if ls.count(ls[s])>=2 or ls.count(ls[s])<1:
            return "False"
    return x[ls.index(max(ls))]





nums = eval(input())
y = search(nums)
print(y)


