ls=input().split()
ls.sort()
count={}
max=0
for s in ls:
    count[s]=ls.count(s)
    if count[s]>max:
        max=count[s]
for k,v in count.items():
    if v==max:
        print('%s %d'%(k,v))
