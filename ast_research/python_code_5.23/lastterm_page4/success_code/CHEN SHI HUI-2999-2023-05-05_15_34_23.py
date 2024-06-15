l=list(input().split())
n,m=input().split()
a,b=int(m),int(n)
c=l[a]
l[a]=l[b]
l[b]=c

print(l)
