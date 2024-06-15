a=list(input().split(' '))
b={}
s=0
for x in a:
    b[x]=b.get(x,0)+1
    if b[x]>s:
        s=b[x]
for f,v in b.items():
    if v==s:
        print(f,v)
