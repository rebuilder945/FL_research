ls1=eval(input())
ls1=list
n,m=eval(input())
ls2=[]
if (n+1)<=len(ls1):
    ls2.append(ls1[n])
    ls2*m
    ls1.extend(ls2)
    print(ls1)
else:
    print("error")
