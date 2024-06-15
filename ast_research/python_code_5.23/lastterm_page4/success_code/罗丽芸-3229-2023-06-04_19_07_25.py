ls=eval(input())
ls1=[]
for x in ls:
    a=ls.count(x)
    if a==1:
        ls1.append(x)
        ls1.sort()
        print(ls1)
else:
    print(False)


