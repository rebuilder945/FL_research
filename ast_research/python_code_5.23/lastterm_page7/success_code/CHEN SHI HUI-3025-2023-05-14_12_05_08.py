n=input().split( )
n.sort()
d={}
c=[]
for i in n:
    d[i]=n.count(i)
    c.append(n.count(i))
for k,v in d.items():
    if v==max(c):
        print(k,v)
