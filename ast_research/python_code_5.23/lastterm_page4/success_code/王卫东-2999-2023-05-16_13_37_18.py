b=input()
a=[str(n) for n in b.split()]
n,m=map(int,input().split())
if  abs(n)<=len(a) and abs(m)<=len(a):
    a[n],a[m]=a[m],a[n]
    print(a)
else:
    print(a)        
