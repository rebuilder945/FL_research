nnames1=str(input())
nnames=nnames1.split(",")
nscores=eval(input())
biao=[]
for x in range(len(nnames)):
    x_biao=[]
    x_biao.append(nnames[x])
    x_biao.append(nscores[x])
    biao.append(x_biao)
print(biao)
