ls=list(input().split())
dic={}
dic1={}
for i in ls:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    for x in dic:
        if dic[i]>=dic[x] and i!=x:
            dic1[i]=dic[i]
sorted_keys = sorted(dic1.keys())
for i in dic1:
    print(f"{i} {dic1[i]}")
    
