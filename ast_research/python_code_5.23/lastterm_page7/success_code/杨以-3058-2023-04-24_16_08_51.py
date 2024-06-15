scount={}
ls=[]
while 1:
    a=input()
    ls.append(a)
    if a=="q":
        break
for i in ls:
    scount[i]=scount.get(i,0)+1
sls=list(scount.items())
sls.sort(key=lambda x:x[1],reverse=True)
print(sls[0][0],sls[0][1])



