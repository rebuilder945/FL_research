item=list(input().split())
dic={}
db=[]
for i in item:
    dic[i]=dic.get(i,0)+1
a=0
for i in dic:
    if dic[i]>a:
        a=dic[i]
for i in dic:
    if dic[i]==a:
        db.append(i,a)
print("/n".join(sorted(db)))
