x=input() or "q"
count={}
while( x!="q"):
    count[x]=count.get(x,0)+1
    x=input() or "q"
countList=list(count.items())
countList.sort(key=lambda x:x[1],reverse=True)
print(countList,countList[0])

