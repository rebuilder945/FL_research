s=input() or 'q'
m={}
while (s!='q'):
    m[s]=m.get(s,0)+1
    s=input() or 'q'
ls=[]
for k,v in m.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
print(ls[0][0],ls[0][1],end="")
