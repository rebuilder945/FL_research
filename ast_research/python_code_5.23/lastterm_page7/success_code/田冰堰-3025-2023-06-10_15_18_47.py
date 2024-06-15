ls=input().split()
ls.sort()
count={}
for s in ls:
    count[s]=ls.count(s)
for k,v in count.items():
    if v==max(count.values()):
        print('%s %d'%(k,v))
