a=list(input().split(' '))
dic={}
for i in a:
    dic[i]=dic.get(i,0)+1
b=list(dic.values())
c=max(b)
d=[]
for i in dic:
    if dic[i]==c:
        d.append(i)
d.sort()
for i in d:
    print(i,dic[i])
