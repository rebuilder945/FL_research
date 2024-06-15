l=input().split()
ls1=list(l)
n,m=map(int,input().split())
ls2=ls1.copy()
ls2[n]=ls1[m]
ls2[m]=ls1[n]
print(ls2)
