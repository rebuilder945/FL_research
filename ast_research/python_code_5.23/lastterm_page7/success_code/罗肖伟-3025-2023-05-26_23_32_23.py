s=input().split()
count={}
for i in s:
    count[i]=count.get(i,0)+1
countlist=list(count.items())
countlist.sort(key=lambda x:x[1],reverse=True)
for i in range(len(countlist)):
    if countlist[i][1]==countlist[0][1]:
        print(countlist[i][0],countlist[i][1]) 
