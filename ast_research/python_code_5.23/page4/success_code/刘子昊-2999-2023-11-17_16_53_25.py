a=input().split()
ls1=list(a)
n,m=map(int,input().split())
ls2=list(a)
p=ls2[m]
q=ls2[n]
ls1[n]=p
ls1[m]=q
print(ls1)


