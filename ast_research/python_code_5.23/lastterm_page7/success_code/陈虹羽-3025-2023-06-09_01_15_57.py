a=print(input().split())
a.sort()
b={}
c=0
for i in a:
    b[i]=b.get(i,0)+1
for i in b:
    if b[i]>c:
        c=b[i]

for i in b:
    if b[i]==c:
        print(i,c)


