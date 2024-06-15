str=input() or 'q'
strdic={}
while(str!='q'):
    strdic[str]+=1
    str=input() or 'q'
countlist=list(strdic.values())
a=max(countlist)
for i in strdic:
    if strdic[i]==a:
        print(i,a)

