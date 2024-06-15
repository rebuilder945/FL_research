a = input().split()
b = {}
c = []
for x in a:
    b[x]=b.get(x,0)+1
for k,v in b.items():
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse = True)
d = []
for i in c:
    if i[1]==c[0][1]:
        print(*i,sep=',')    


