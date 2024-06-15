x=input().split()
count={}
for i in x:
    count[i]=count.get(i,0)+1
ls=[]
a=max(count.values())
for k,v in count.items():
    if v==a:
        print(k,v)
