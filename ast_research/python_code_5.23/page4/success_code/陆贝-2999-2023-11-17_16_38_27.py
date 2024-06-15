ls=input().split(sep=" ")
aa=input().split(sep=" ")
n=eval(aa[0])
m=eval(aa[-1])
t1=ls[m]
t2=ls[n]
ls[m]=t2
ls[n]=t1
print(ls)
