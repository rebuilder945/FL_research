x=input().split()
count={}
for i in x:
    count[i]=count.get(i,0)+1
ls=[]
a=max(count.values())
for k,v in count.items():
    if v==a:
        ls.append([k,v])
ls.sort(key=lambda x:x[0])
for i in ls:
    str=i[0]
    num=i[1]
    print(str,num)
