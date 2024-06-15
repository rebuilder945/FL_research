a = eval(input())
res = []
for i in a:
    k=a.count(i)
    for i in range(k):
        if k >1:
            res.append(i)
print(res)
