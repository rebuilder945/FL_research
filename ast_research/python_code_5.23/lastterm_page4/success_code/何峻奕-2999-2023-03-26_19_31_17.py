a=input().split(" ")
n=int,input().split(" ")
for i,j in n:
    a1=a.copy()
    a[i],a[j]=a[j],a[i]
print(a)
