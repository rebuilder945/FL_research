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
ls2=[]
for x in lst:
    ls2.append(x[1])
a=max(ls2)
ls1=[]
for x in range(len(lst)):
    if lst[x][1]==a:
        ls1.append(lst[x][0])
    else:
        break
ls1.sort()
for x in ls1:
    print(x,a)
