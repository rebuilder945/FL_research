b=[]
c=[]
d=[]
while True:
    m=input().split()
    b.append(m)
    if m==['ok']:
        break
del b[-1]
b.sort()
for x in range(len(b)):
    c.append(b[x][0])
    d.append(int(b[x][1]))
print(c)
d.sort()
print(d)
GDP=dict(b)
if'India'not in GDP:
    print("no")
else:
    print("yes")
print(sum(d))
