


ls=[]
dic={}
a=input() or "p"
while a!="p":
    ls.append(a)
    a=input() or "p"
for x in ls:
    if x not in dic.keys():
        dic[x]=1
    else:
        dic[x]+=1
for x in dic.keys():
    if dic[x]==max(dic.values()):
        print(x,dic[x])


