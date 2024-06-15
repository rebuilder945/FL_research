l=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
h=l
h[n],h[m]=l[m],l[n]
print(h)

