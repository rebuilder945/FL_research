m=input().split("")
n=[]
a=[]
for x in m:
    n.append((x,m.count(x)))
    a.append(m.count(x))
n=dict(n)
for k,v in n.items():
    if v ==max(a):
        print(k,v)


