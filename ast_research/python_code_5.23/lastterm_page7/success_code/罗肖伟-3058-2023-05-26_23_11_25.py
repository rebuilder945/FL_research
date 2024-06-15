s=input() or "q"
count={}
while s!="q":
    count[s]=count.get(s,0)+1
    s=input() or "q"
countlist=list(count.items())
countlist.sort(key=lambda x:x[1],reverse=True)
print(countlist[0][0],countlist[0][1])
