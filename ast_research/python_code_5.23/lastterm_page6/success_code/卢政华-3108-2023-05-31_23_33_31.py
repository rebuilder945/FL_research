str=input().split
a={}
for i in str:
    for x in i:
        if x not in a:
            a[x]=1
        else:
            a[x]+=1
a=sorted(a.items(),key=lambda x:x[0])
print(a)
