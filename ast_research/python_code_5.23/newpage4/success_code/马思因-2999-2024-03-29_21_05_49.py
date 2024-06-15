a=input().split(" ")
b=list(map(int,input().split(" ")))
n=b[0]
m=b[1]
c=a[n]
a[n]=a[m]
a[m]=c
print(a)

