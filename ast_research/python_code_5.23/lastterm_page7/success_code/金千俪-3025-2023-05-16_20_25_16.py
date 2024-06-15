a=input().split(" ")
dic={}
for i in a:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1
b=max(dic.values())
dicSort  = dict(sorted(dic.items(),key=lambda x:x[0]))
for k in dicSort:
    if dicSort[k]==b:
        print(k,b)
