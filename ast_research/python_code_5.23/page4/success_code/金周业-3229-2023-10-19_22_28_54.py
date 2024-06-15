ls=eval(input())
for i in ls[:]:
    if ls.count(i) > 1:
        ls.remove(i)
lst=sorted(ls)
lsm=''
lsm=str(lst[1])
for j in range(1,len(lst)):
    lsm=lsm+","+str(lst[j])
print(lsm)

