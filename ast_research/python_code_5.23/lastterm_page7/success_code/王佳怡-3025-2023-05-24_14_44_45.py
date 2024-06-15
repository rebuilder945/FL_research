a=input().split()
counts={}
for i in a:
    counts[i]=counts.get(i,0)+1
l=list(counts.items())
l.sort(key=lambda x:x[1],reverse=True)
b=l[0][1]
for x in range(len(l)):
    if l[x][1]==b:
        print(l[x][0],end=" ")
        print(l[x][1])
