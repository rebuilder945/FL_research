ls=input().split()
ls2=list(map(int,input().split()))
n,m=ls2[0],ls2[1]
ls[n],ls[m]=ls[m],ls[n]
print(ls)
