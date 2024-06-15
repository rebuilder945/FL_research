dic={}
a=input().split()
for i in a:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
b=[]
for i in dic:
    b.append(dic[i])
cishu=max(b)
c=list(dic.keys())
c.sort(key=a)
for i in c:
    if dic[i]==cishu:
        print(i,cishu)

