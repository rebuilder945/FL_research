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
for i in dic.keys():
    if dic[i]==cishu:
        print(i,cishu)

