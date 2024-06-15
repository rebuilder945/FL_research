n=int(input())
v1=list(x for x in range (1,n+1))
for x in v1:
    if x==n:
        v1[n-1]=1
    if x<n:
        v1[x-1]=x+1
print(v1)
