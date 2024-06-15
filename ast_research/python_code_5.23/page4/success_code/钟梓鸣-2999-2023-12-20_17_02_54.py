a=input().split(" ")
print(a)
n=input(end=' ')
m=input()
n=int(n)
m=int(m)
temp=a[n]
a[n]=a[m]
a[m]=temp
print(a)
