strl=input().split()
dic={}
for i in strl:
    dic[i]=dic.get(i,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse =True)
lst1=lst[0]
maxnum=lst1[1]
lst.sort(key=lambda x:x[0],reverse =True)
for i in lst:
    if i[1]==maxnum:
        print(i[0],i[1])


