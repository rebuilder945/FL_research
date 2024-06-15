ls=list(input().split())
a,b=map(int,input().split())
ls[a],ls[b]=ls[b],ls[a]
print(ls)
