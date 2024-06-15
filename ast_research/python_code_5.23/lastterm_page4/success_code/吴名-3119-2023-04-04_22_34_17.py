a=eval(input())
b=[]
c=[]
d=[]
for i in range(len(a),0,-1):
    n=a[i-1]
    b.append(n)
for x in b:
    if x not in c:
        c.append(x)
for y in range(len(c),0,-1):
    m=c[y-1]
    d.append(m)
print(d)
