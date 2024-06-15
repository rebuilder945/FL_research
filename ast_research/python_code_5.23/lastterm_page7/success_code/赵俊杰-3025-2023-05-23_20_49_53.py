ls=input().split(" ")
dic={}
for i in ls:
    dic[i]=dic.get(i,0)+1
ls1=[]
for k,v in dic.items():
    ls1.append([k,v])
ls1.sort(key=lambda x:x[1],reverse=True)
a=ls1[1][1]
for x in ls:
    if x[1]>=a:
        print(x)
    else:
        pass
