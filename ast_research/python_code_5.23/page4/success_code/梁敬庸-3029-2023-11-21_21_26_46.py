a=input().split()
b=input().split()
m=[]
for x in range(len(b)):
    n=[]
    n.append(a[x])
    n.append(eval(b[x]))
    m.append(n)
print(m)
