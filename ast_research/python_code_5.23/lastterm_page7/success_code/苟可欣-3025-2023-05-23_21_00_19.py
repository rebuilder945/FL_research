ls=input().split()
dic={}
for x in ls:
    if x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]=1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])
for x in range(1,len(lst)):
    if lst[x][1]==lst[0][1]:
        print(lst[x][0],lst[x][1])
    else:
        break
