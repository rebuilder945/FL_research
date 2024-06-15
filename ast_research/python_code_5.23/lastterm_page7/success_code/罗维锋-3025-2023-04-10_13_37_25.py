a=input().split()
dic={}
for x in a:
    if x not in dic.keys():
        dic[x]=a.count(x)
b=max(dic.values())
for i in dic:
    if dic[i]==b:
        print(i,dic[i])
