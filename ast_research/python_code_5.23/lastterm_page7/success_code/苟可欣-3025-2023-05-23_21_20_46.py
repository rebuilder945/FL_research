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
lst.sort(key=lambda x:x[1])
ls1=[]
for x in range(1,len(lst)):
    if lst[x][1]==lst[-1][1]:
        ls1.append(lst[x][0])
    else:
        break
ls1.sort()
for x in ls1:
    print(x,lst[-1][1])
