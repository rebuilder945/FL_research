a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
dic={}
for i in b:
    dic[i]=a.count(i)
lst=list(dic.items())
for i in range(0,len(lst)):
    lst[i]=list(lst[i])
c=[lst[x][1] for x in range(0,len(lst))]
d=max(c)
for i in lst:
    if i[1]!=d:
        lst.remove(i)
lst.sort(key=lambda x:x[0])
for i in range(0,len(lst)):
    print(lst[i][0],d)

