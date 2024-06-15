n=input().split()
dic={}
for i in n:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max=max(dic.values())
for r,num in dic.items():
    if num==max:
        print(r,num)
 

