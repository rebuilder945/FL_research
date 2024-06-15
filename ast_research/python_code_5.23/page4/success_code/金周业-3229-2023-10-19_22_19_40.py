ls=eval(input())

for i in ls[:]:
    if ls.count(i) > 1:
        ls.remove(i)
ls1=sorted(ls)
ls2=','.join(ls1)
print(ls1)

