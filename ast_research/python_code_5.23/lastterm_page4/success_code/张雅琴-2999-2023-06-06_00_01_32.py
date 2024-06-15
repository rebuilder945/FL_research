a=input().split()
b=input().split()
n=int(b[0])
m=int(b[1])
if n<len(a) and m<len(a):
    a[n],a[m]=a[m],a[n]
print(a)
