s=input() or "q"
Count={}
while(s !="q"):
    Count[s]=Count.get(s,0)+1
    s=input("") or "q"
CountList=list(Count.items())
CountList.sort(key=lambda x:x[1],reverse=True)
print(*CountList[0])

