n=input().split()
dic={}
for x in n :
    dic[x]=dic.get(x,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
lst1=[]
for i in lst:
    lst1.append(i[1])
m=max(lst1)
lst2=[]
for i in lst:
    if i[1]==m:
        lst2.append(i)
lst2.sort(key=lambda x:x[0])
for i in lst2:
    print(i[0],i[1])

