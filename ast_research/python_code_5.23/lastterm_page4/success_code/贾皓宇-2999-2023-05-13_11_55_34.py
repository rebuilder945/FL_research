a=list(input().split(' '))
n,m=eval(input())
b=a.copy()
b[n]=a[m]
b[m]=a[n]
print(b)
