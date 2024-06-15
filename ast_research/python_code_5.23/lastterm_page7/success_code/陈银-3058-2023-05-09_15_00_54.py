
m={}
b = []
while True:
    a = input()
    b.append(a)
    if a =="q":
        break
for x in b:
    m[x]=m.get(x,0)+1
c = []
for k,v in m.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse=True)
print(*c[0],sep=" ")


