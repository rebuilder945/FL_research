a=list(map(int,input().split(",")))
n,m=eval(input())
a[n],a[m]=a[m],a[n]
print(a)
