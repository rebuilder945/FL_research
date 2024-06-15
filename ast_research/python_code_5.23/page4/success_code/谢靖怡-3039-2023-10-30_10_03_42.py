ls=eval(input())
maxnum=max(ls)
minnum=min(ls)
for i in ls:
    if i==maxnum:
        ls.remove(i)
    else:
        break
for x in ls:
    if x==minnum:
        ls.remove(x)
    else:
        break
print(list(ls))
