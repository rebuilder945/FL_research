a=input()
a=a.split(' ')
b=input()
b=b.split(' ')
n=int(b[0])
m=int(b[1])
x=a[n]
y=a[m]
a[n]=y
a[m]=x
print(a)
