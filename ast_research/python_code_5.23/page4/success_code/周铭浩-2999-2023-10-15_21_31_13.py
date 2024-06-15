a=input()
a=a.split(' ')
print(a)
n,m=eval(input())
x=a[n]
y=a[m]
a[n]=y
a[m]=x
print(a)
