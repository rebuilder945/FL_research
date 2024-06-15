a=input().split()
n,m =map(int,input().split())
if -len(a)<=n<len(a) and -len(a)<=m<len(a):
    a[n],a[m]=a[m],a[n]
print(a)
