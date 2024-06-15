ls=input().split()
n,m=eval(input())
ls2=ls[::]
ls2[n]=ls[m]
ls2[m]=ls[n]
print(ls2)
