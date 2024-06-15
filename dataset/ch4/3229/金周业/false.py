ls=eval(input())
for i in ls[:]:
    if ls.count(i) > 1:
        ls.remove(i)
lst=sorted(ls)
lsm=''


for j in range(len(lst)):
    if j == 0:
        lsm=str(lst[j])

    else:
        lsm=lsm+","+str(lst[j])
print(lsm)

