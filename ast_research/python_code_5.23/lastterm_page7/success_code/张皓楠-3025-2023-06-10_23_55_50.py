m=list(input().split(' '))
dic={}
for i in m:
    dic[i]=m.count(i)
b=max(dic.values())
c=[]
for i in dic:
    if dic[i]==b:
        c.append(i)
        c.sort()
for i in c:
    print("{} {}".format(i,b))

