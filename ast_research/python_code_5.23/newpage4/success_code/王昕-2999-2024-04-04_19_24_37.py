n=list(map(str,input().split(" ")))
a,b=input().split(" ")
a=int(a)
b=int(b)
c=n[a]
d=n[b]
n[a]=d
n[b]=c
print(n)

