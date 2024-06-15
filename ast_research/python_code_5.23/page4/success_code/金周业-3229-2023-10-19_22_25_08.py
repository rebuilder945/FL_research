ls=eval(input())
for i in ls[:]:
    if ls.count(i) > 1:
        ls.remove(i)
lst=sorted(ls)
lsm=''
for j in lst:
    lsm=lsm+",+j"
print(lsm)

