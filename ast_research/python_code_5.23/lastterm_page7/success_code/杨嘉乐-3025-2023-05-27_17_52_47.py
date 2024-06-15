fuck=list(input().split(" "))
dick={}
for i in fuck:
    if i in dick:
        dick[i]+=1
    else:
        dick[i]=1
mm=max(dick)
for i in fuck:
    if fuck[i]==mm:
        print("%s %d"%(i,fuck[i]))
