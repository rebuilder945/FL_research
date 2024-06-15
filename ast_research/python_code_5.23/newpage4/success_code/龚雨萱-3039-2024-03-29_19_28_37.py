ls=list(eval(input()))
maxnum=max(ls)
minnum=min(ls)
lsCopy=ls.copy()
for i in ls:
    if i==maxnum or i==minnum:
        lsCopy.remove(i)
print(lsCopy)
