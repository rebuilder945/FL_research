lst=input().split()
dic={}
for i in lst:
    dic[i]=dic.get(i,0)+1
diclist=[]
for k,v in dic.items():
    diclist.append([k,v])
diclist.sort(key=lambda x:x[1],reverse=True)
result=[]
for i in diclist:
    if i[1]==diclist[0][1]:
        result.append(i)
result.sort(key=lambda x:x[0])
for i in result:
    print(i[0],i[1])
