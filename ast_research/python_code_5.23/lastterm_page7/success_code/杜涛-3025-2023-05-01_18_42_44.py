a=input().split()
dic={}
for i in a:
    dic[i]=dic.get(i,0)+1
lst=list(dic.items())
lst.sort(key=lambda x:x[1],reverse=True)
lst1=[]
for i in range(len(lst)):
    if lst[i][1]==lst[0][1]:
        lst1.append(lst[i])
lst1.sort(key=lambda x:x[0],reverse=False)
for x in lst1:
    print(x[0],x[1])

