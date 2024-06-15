str=input().split()
strdic={}
for i in str:
    strdic[i]=str.count(i)
countlist=list(strdic.values())
a=max(countlist)
for i in strdic:
    if strdic[i]==a:
        print(i,a)
