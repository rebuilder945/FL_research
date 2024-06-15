ls=input().split(",")
dic1={}
for x in ls:
    if x in ls:
        dic1[x]+=1
    else:
        dic1[x]=1
num=list(dic1.values())
big=max(num)
for t in dic1.keys():
    if dic1[t]==big:
        print(t,big)
