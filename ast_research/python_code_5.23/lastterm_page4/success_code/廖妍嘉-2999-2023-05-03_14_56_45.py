ls=input().split()
n,m=map(int,input().split())
ls2=ls[::]
ls2[n]=ls[m]
ls2[m]=ls[n]
print(ls2)
