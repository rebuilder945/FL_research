a=input().split()
b={}
for x in a:
    b[x]=b.get(x,0)+1
a=list(b.items())
a.sort(key=lambda x:x[1],reverse=True)
n=a[0][1]
b=[]
for x in a:
    if x[1]==n:
        b.append(x[0])
b.sort()
for x in b:
    print(x,n)

