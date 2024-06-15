a=input()
a=a.split()
n,m=map(int,input().split())
a[n],a[m]=a[m],a[n]
print(a)
