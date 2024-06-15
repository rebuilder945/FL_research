a=input().split(" ")
n=int,input().split(" ")
a1=a.copy()
for i in n:
    a[i],a[i+1]=a[i+1],a[i]
    print(a)
