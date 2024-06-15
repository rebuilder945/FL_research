ls1 = input().split(",")
ls3 = []
n,m = eval(input())
for y in ls1:
    z=int(y)
    ls3.append(z)
c=[]
if n<len(ls1) and n>0:
    a=ls1[n-1]*m
    for i in a:
        x=int(i)
        c.append(x)
    ls3.remove(ls3[n-1])
    ls2=ls3+c
    print(ls2)
elif n<0 and -n<=len(ls1):
    a=ls1[n]*m
    for i in a:
        x=int(i)
        c.append(x)
    ls3.remove(ls3[n])
    ls2=ls3+c
    print(ls2)
else:
   print("error")

