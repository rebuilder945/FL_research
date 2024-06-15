a=list(map(str,input().split()))
b,c=map(int,input().split())
t=a.copy()
t[b]=a[c]
t[c]=a[b]
print(t)
