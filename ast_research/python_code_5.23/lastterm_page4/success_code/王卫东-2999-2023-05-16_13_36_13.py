b=input()
a=[str(n) for n in b.split()]
n,m=map(int,input().split())
if n>=0 and n<=len(a) and m>=0 and m<=len(a):
    a[n],a[m]=a[m],a[n]
    print(a)
else:
    print(a)        
