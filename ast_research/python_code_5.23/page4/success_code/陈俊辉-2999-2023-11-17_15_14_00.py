a=list(map(str,input().split(' ')))
n,m=map(int,input().split(' '))
b.copy(a)
b[m]=a[n]
b[n]=a[m]
print(b)
