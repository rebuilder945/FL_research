a=list(map(str,input().split(" ")))
b=input().split(" ")
n=eval(b[0])
m=eval(b[1])
c=a[n]
d=a[m]
a[n]=d
a[m]=c
print(a)
