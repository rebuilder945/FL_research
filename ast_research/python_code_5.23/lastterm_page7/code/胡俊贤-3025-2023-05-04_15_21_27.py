s=input().split()
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
lsvalue=dic.values()
M=max(lsvalue)
ls=list(dic.items())
ls.sort(key=lambda x:x[0] reverse=False)
for i in ls:
    if i[1]==M:
        print(i[0],i[1])


        


