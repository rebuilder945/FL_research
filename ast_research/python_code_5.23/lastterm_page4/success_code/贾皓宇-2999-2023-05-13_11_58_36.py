a=list(input().split(' '))
n,m=input().split(' ')
b=a.copy()
b[n]=a[m]
b[m]=a[n]
print(b)
