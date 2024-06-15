lst=eval(input())

dic={}
for i in range(len(lst)):
    dic[lst[i]]=i

ans=[]
for i in range(len(lst)):
    if(dic[lst[i]]==i):
        ans.append(lst[i])
print(ans)

