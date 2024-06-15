str=input().split()
strdic={}
for i in str:
    strdic[i]=str.count(i)
countlist=list(strdic.values())
a=max(countlist)
b=[]
for i in strdic:
    if strdic[i]==a:
        b.append(i)
b.sort()
for i in b:
    print(i,a)
