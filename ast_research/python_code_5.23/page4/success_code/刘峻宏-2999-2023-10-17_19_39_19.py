


a=list(input().split(' '))
b=list(input().split(' '))
m=eval(b[0])
n=eval(b[1])
a[m],a[n]=a[n],a[m]
print(a)
