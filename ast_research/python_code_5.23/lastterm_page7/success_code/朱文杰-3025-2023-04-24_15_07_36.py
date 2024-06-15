Str=input().split()
dic={}
for i in Str:
    dic[i]=dic.get(i,0)+1
ls=list(dic.values())
for i in dic:
    if dic[i]==max(ls):
        print(i,max(ls))
