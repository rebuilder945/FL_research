ls=eval(input())
ls=list(ls)
ls1=ls.copy()
for x in ls:
    if x==0:
        ls1.remove(x)
        ls1.append(x)
print(ls1)

