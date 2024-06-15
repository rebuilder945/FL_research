ls=input().split()
a=input().split()
n,m=int(a[0]),int(a[1])
ls[n],ls[m]=ls[m],ls=[n]
print(ls)
