a=input()
n,m=map(int,(input().split()))
a=a.split()
b=a[n]
a.insert(m,b)
if m>=0:
    d=a.pop(m+1)
else:
    d=a.pop(m)
a.insert(n,d)
if n>=0:
    f=a.pop(n+1)
else:
    f=a.pop(n)
print(a)
