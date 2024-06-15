ls=input().split()
n,m=map(int,input().split())
#print(n,m)
ls[n],ls[m]=ls[m],ls[n]
print(ls)
