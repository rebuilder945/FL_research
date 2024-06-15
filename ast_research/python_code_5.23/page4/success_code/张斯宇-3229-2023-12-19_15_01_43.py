lst=eval(input())

dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else: dic[i]+=1

ans=[]
for i in lst:
    if dic[i]==1:
        ans.append(i)

ans.sort()
len=len(ans)
if len==0: print("False")
else: 
    print(",".join(map(str,ans)))
