str=input() or 'q'
strlist=[]
while(str!='q'):
    strlist.append(str)
    str=input() or 'q'
strdic={}
for i in strlist:
    strdic[i]=strlist.count(i)
countlist=list(strdic.values())
a=max(countlist)
for i in strdic:
    if strdic[i]==a:
        print(i,a)

