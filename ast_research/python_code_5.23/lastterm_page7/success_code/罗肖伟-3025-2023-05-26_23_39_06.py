s=input().split()
count={}
for i in s:
    count[i]=count.get(i,0)+1
countlist=list(count.items())
countlist.sort(key=lambda x:x[1],reverse=True)
countlist1=[]
for i in range(len(countlist)):
    if countlist[i][1]==countlist[0][1]:
       countlist1.append(countlist[i])
countlist1.sort(key=lambda x:x[0])
for x in countlist1:
    print(x[0],x[1]) 
