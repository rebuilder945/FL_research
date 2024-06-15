a = input().split()
ls = list(map(int,input().split()))
m = ls[0]
n = ls[1]
a[n],a[m]=a[m],a[n]
print(a)


