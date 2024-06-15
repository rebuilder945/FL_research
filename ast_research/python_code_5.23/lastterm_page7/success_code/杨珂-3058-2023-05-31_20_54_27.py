dic={}
a=input() or "q"
while a!="q":
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
    a=input() or "q"
b=[]
for i in dic:
    b.append(dic[i])
cishu=max(b)
for i in dic.keys():
    if dic[i]==cishu:
        print(i,cishu)

