ls=eval(input())
maxnum=max(ls)
minnum=min(ls)
for i in range(ls):
    if i==maxnum:
        ls.remove(i)
    else:
        break
for x in range(ls):
    if x==minnum:
        ls.remove(x)
    else:
        break
print(ls)
