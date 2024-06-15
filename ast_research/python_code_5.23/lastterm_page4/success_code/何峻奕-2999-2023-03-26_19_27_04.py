a=input().split(" ")
b,c=int,input().split(" ")
a1=a.copy()
a[b],a[c]=a[c],a[b]
print(a)
