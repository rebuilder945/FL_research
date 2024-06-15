a=input()
b='a'
for i in a:
    b += i
    c=b[1:]
d=[]
for r in c:
    if not r in d:
        e=c.count(r)
        print("%s,%d"%(r,e))
        d.append(r)

