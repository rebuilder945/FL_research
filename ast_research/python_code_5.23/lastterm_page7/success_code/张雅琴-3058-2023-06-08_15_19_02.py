a=input() or "q"
b=[]
while a!="q":    
    b.append(a)
    a=input() or "q"
c=[]
for i in b:
    if i not in c:
        c.append(i)
dic={}
for x in c:
    dic[x]=b.count(x)
lst1=list(dic.items())
for i in range(0,len(lst1)):
    lst1[i]=list(lst1[i])
lst1.sort(key=lambda x:x[1])
lst2=lst1[-1]
for i in lst2:
    print(i,end=" ")    

