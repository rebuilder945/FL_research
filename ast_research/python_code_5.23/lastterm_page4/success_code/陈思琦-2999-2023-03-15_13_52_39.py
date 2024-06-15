a=input()
a=list(a)
n,m=map(int,input().split())
a[n],a[m]=a[m],a[n]
print(a)
