ls=eval(input())
ls1=[]
for x in ls:
    a=ls.count(x)
    if a==1:
        ls1.append(x)
    if a==0:
        print(False)
ls1.sort
ls1=list(map(str,ls1))
print(ls1)

