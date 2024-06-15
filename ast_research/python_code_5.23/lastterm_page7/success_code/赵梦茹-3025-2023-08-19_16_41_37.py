a=input().split(" ")
dic={}
for i in a :
    dic[i]=a.count(i)
jishu=0
b=max(dic.values())
c=[]
for i in dic:
    if dic[i]==b:
        c.append(i)
c.sort()
for i in c:
    print("{} {}".format(i,b))
