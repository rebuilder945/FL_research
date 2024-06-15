a=list(input().split(' '))
b={}
s=0
for x in a:
    b[x]=b.get(x,0)+1
    if b[a]>s:
        s=b[a]
for f,v in b.items():
    if v==s:
        print(f,v)
