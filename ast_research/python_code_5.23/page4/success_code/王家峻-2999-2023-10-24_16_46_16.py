n=input()
n=list(n.split())
a,b=input().split()
a=int(a)
b=int(b)
n[b],n[a]=n[a],n[b]
n=list(n.split())
print(n)
