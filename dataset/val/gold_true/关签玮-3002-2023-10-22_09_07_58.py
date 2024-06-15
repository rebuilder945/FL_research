lst=eval(input())
a=sum(lst)/len(lst)
b=str(a)
ls1=list(b)
if int(ls1[-1])==0:
    for i in ls1[0:-2]:
        print(i,end="")
else:
    c="%.2f"%(a)
    print(c)
