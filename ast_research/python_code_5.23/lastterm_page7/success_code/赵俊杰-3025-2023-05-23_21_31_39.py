ls=input().split(" ")
dic={}
for i in ls:
    dic[i]=dic.get(i,0)+1
ls1=[]
for k,v in dic.items():
    ls1.append([k,v])
ls1.sort(key=lambda x:x[1],reverse=True)
a=int(ls1[1][1])
for n in ls1:
    if n[1]>=a:
        print("%s %d"%(n[0],n[1]))
    else:
        pass
