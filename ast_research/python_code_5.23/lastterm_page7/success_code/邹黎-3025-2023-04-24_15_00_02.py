
lst=list(input().split())
dic={}
lst0=[]
for x in lst:
    dic[x]=lst.count(x)
b=max(dic.values())

for key, value in dic.items():
    if value==b:
        lst0.append(key)
lst0.sort()
for x in lst0:
    print(x,b)

