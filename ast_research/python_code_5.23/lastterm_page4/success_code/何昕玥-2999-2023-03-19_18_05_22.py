def Change(a,b,c):
    a[b],a[c]=a[c],a[b]
    print(a)
sum=input()
b,c=list(map(int,input().strip().split()))
a=sum.split()
Change(a,b,c)
