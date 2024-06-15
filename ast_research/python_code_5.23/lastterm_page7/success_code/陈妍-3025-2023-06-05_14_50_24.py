sList=input().split()
Count={}
Max=0
for s in sList:
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
CountList=list(Count.items())
CountList.sort()
CountList.sort(key=lambda x:x[1],reverse=True)
for k,v in CountList:
    if v==Max:
        print(k,v)

