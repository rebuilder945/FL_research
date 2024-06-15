fuck=list(input().split(" "))
dick={}
for i in fuck:
    if i in dick:
        dick[i]+=1
    else:
        dick[i]=1
fuck.sort()
mm=max(dick.values())
for i in fuck:
    if dick[i]==mm:
        print("%s %d"%(i,dick[i]))
        dick[i]-=1
