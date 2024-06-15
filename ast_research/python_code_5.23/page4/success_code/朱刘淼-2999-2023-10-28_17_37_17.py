ls=input().split()
n,m=list(map(int,input().split()))
ls[n],ls[m]=ls[m],ls[n]
print(ls)
