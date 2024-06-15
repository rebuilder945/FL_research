nnames1=str(input())
nnames=nnames1.split(",")
nscores1=str(input())
nscores=nscores1.split(",")
biao=[]
for x in range(len(nnames)):
    x_biao=[]
    x_biao.append(nnames[x])
    x_biao.append(int(nscores[x]))
    biao.append(x_biao)
biao_sorted=sorted(biao,key=lambda x:x[1])
print(biao_sorted)
