a = input().split()
b = {}
ls = []
for i in a:
    b[i] = b.get(i,0)+1
for k,v in b.items():
    ls.append([k,v])
ls1 = ls.copy()
ls1.sort(key=lambda x:x[0])
ls1.sort(key=lambda x:x[1])
c=ls1[-1][1]
for x in ls:
    if x[1]==c:
        print(x[0],x[1])
    



