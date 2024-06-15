d={}
i=input()
while i!="q":
    if i in d:
        d[i]+=1
        continue
    else:
        d[i]=1
        continue
b=0
for j in d.values():
    if j>b:
        b=1
    for k in d.keys():
        if d[k]==b:
            print("{}{}.format(i,b)")
