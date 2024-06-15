a = input().split()
b = {}
ls = []
for i in a:
    b[i] = b.get(i,0)+1
for k,v in b.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1])
c=ls[-1][1]
for x in ls:
    if x[1]==c:
        print(x[0],x[1])
    



