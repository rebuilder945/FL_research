ls=eval(input())
n,m=eval(input())
a=len(ls)
ls1=[]
if n>=a:
    print("error")
else:
    for i in range(a):
        if i==n:
            b=ls[i]
    ls1.append([b]*m)
    print(ls+ls1)
