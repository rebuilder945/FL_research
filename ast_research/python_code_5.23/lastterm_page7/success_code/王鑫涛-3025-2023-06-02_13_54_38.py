a=input().split(' ')
b={}
c=1
for i in a:
    b[i]=a.count(i)
    if a.count(i)>c:
        c =a.count(i)
b.sort()
for r in b:
    if b[r]==c:
        print('%s %d'%(r,b[r]))
