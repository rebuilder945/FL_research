ls=input().split(" ")
dic={}
for i in ls:
    dic[i]=dic.get(i,0)+1
ls1=[]
for k,v in dic.items():
    ls1.append([k,v])
ls2=sorted(ls1,key=lambda x:(-x[1],x[0]),reverse=False)
a=int(ls2[0][1])
for n in ls2:
    if n[1]>=a:
        print("%s %d"%(n[0],n[1]))
    else:
        pass
