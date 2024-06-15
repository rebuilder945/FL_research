lst=eval(input())
a=sum(lst)/len(lst)
print(a)
b=str(a)
ls1=list(b)
if int(ls1[-1])==0:
    for i in ls1[0:-2]:
        print(i,end="")
else:
    print(round(a,2))
