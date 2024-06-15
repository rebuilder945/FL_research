string=input().split(' ')
dic={}
for x in string:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
n=0;names=[]
for s in dic:
    if dic[s]>n:
        n=dic[s]
for x in dic:
    if dic[x]==n and x not in names:
        names.append(x)
names.sort()
for x in names:
    print(x,n)
