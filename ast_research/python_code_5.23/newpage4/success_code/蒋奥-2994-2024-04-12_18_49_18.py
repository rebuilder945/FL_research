ls1 =list(eval(input()))
n,m=eval(input())
c=[]
if n<len(ls1) and n>0:
    a=ls1[n-1]
    c.append(a)
    ls2=c*m
    ls3=ls1+ls2
    ls3.remove(a)
    print(ls3)
elif n<0:
    a=ls1[n]*m
    c.append(a)
    ls2=c*m
    ls3=ls1+ls2
    ls3.remove(a)
    print(ls3)
else:
    print("error")

