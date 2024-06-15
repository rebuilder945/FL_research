ls=eval(input())
maxnum=max(ls)
minnum=min(ls)
ls.remove(maxnum)
ls.remove(minnum)
ls.reverse()
for i in ls:
    if i==maxnum:
        ls.remove(i)
    else:
        break
ls.sort()
for x in ls:
    if x==minnum:
        ls.remove(x)
    else:
        break
print(list(ls))
