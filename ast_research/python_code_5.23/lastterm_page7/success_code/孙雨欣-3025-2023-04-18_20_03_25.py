item=list(input().split())
dic={}
db=[]
for i in item:
    dic[i]=dic.get(i,0)+1
a=0
for i in dic:
    if dic[i]>a:
        a=dic[i]
dic=item.sort(key=lambda x:x[0],reverse=False)
for i in dic:
    if dic[i]==a:
        print(i,a)

