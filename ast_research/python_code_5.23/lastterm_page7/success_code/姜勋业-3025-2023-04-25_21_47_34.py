item=list(input().split())
dic={}
for i in item:
    dic[i]=dic.get(i,0)+1
a=0
for i in dic.keys():
    if dic[i]>a:
        a=dic[i]
b=[]
for k,v in dic.items():
    if dic[k]==a:
        b.append([k,v])
b.sort()
for i in b:
    print(i[0],i[1])
    

