name=input().split()
a,b=map(int,input().split())
t=name[a]
name[a]=name[b]
name[b]=t
print(name)
