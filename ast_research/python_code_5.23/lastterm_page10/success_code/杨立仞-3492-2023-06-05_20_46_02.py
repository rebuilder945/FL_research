str=input()
countlist=[]
for i in str:
    if str.count(i)==1:
        countlist.append(i)
print(countlist[0])
