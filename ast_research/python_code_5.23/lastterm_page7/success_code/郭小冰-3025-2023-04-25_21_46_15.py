zifu=input().split()
dic={}
for i in zifu:
    dic[i]=dic.get(i,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
cishu=[]
for i in lst:
    cishu.append(i[1])  
zuida=max(cishu)
for i in lst:
    if i[1]==zuida:
        print(i[0],i[1])
