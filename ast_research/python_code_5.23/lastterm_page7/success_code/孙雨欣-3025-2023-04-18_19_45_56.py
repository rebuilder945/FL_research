item=list(input().split())
dic={}
for i in item:
    dic[i]=dic.get(i,0)+1
a=0
for i in dic:
    if dic[i]>a:
        a=dic[i]
for i in dic:
    if dic[i]==a:
        print(i,a)
