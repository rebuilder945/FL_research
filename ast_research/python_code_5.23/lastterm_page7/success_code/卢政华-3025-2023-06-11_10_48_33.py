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
for i in b.items():
    if i[1]==c:
        d.append(i)
d.sort()
for item in d:
    print("%s %d" % (item[0], item[1]))
