m=input().split("")
n=[]
for x in m:
    n.append((x,m.count(x)))
n = dict(n)
b= max(n.values)
print(n.keys(b),b)

