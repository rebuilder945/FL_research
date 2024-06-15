a=input()
a=a.split(' ')
n,m=eval(input())
x=a[n]
y=a[m]
a[n]=y
a[m]=x
print(a)
