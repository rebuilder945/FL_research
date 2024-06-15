a=(input())
ls1=a.split(',')
ls5=[]
for x in ls1:
    y=int(x)
    ls5.append(y)
n,m=eval(input())
if n<=len(ls1)-1:
    x=ls5[n]
    ls2=[]
    ls2.append(x)
    ls3=ls2*m
    ls4=ls5+ls3
    print(ls4)
else:
    print('error')
