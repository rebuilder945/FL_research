ls=[]
while True:
    a=input()
    if a!='q':
        ls.append(a) 
    else:
        break
dit={}
for x in ls:
    dit[x]=dit.get(x,0)+1
ls1=[]
for k,v in dit.items():
    ls1.append(k+' '+str(v))
ls1.sort(key=lambda x:x[-1],reverse=True)
print(ls1[0])

