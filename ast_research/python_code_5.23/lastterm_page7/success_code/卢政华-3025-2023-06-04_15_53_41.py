a=input().split()
b={}
c=0
d=[]
for i in list(a):
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
    if c<b[i]:
        c=b[i]
for item in b.items():
    if int(item.values)==c:
        d.dppend(item)
print(d)


