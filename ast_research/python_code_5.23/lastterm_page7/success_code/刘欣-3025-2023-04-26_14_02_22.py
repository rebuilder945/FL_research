ls=list(input().split())
dic={}
for i in ls:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    for x in dic:
        if dic[i]>=dic[x] and i!=x:
            print(f'{i} {dic[i]}')
            break
    
