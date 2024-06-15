a=input().split()
counts={}
l1=[]
for i in a:
    counts[i]=counts.get(i,0)+1
l=list(counts.items())
l.sort(key=lambda x:x[1],reverse=True)
b=l[0][1]
for x in range(len(l)):
    if l[x][1]==b:
        l1.append(l[x])
        l1.sort(key=lambda x:x[0])
for j in range(len(l1)):
    print(l1[j][0],end=" ")
    print(l1[j][1])
