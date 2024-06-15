a=list(map(str,input().split()))
b,c=map(int,input().split())
d=a.copy()
d[b]=d[c]
d[c]=d[b]
print(d)
