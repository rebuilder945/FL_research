m=eval(input())
a=min(m)
b=max(m)
c=[a,b]
d=[]
for x in m:
    if x not in c:
        d.append(x)
print(d)
