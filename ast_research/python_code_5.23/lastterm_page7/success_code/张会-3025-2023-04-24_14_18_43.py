s=input() or 'q'
m={}
while (s!='q'):
    m[s]=m.get(s,0)+1
    s=input() or 'q'
ls=[]
for k,v in m.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(len(ls)):
    if ls[i][1]==ls[0][1]:
        print(ls[i][0],ls[i][1])
