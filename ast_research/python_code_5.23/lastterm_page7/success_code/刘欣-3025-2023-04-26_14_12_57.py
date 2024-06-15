ls=list(input().split())
dic={}
for i in ls:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max_count=max(dic.values())
max_str=sorted([key for key, value in dic.items() if value == max_count])
for string in max_str:
    print(string, max_count)
