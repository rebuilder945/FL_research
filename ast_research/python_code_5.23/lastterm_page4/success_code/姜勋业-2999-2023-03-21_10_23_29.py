a=input().split(" ")
m,n=input().split(" ")
m=eval(m)
n=eval(n)
i=a[m]
j=a[n]
a[m]=j
a[n]=i
print(a)
