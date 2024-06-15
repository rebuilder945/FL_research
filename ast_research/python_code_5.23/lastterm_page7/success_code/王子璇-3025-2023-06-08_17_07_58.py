string=input().split(' ')
dic={}
for x in string:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
n=0;names=[]
for s in dic:
    if dic[s]>=n:
        n=dic[s]
        names.append(s)

namesort=names.sort()
for name in namesort:
    print(name,n)
