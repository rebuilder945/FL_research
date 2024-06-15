dic={}
b=[]
a=input().split()
for x in a:
    if x not in dic.keys():
        dic[x]=1
    else:
        dic[x]+=1
for x in dic.keys():
    if dic[x]==max(dic.values()):
        b.append(x)
b.sort()
for x in b:
    print(x,dic[x])

