sList=input().split()
count={}
Max=0
for s in sList:
    count[s]=count.get(s,0)+1
    if count[s]>Max:
        Max=count[s]

countList=list(count.items())
countList.sort()
for k,v in countList:
    if v == Max:
        print(k,v)


