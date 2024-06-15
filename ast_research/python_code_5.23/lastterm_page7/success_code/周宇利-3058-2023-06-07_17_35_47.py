d={}
i=input()
while i!="q":
    if i in d:
        d[i]+=1
    else:
        d[i]=1
i=input()
b=0
for i in d.values():
    if i>b:
        b=1
    for i in d.keys():
        if d[i]==b:
            print("{}{}.format(i,b)")
