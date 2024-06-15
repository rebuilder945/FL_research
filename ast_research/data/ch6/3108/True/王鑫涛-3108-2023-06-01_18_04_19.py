a=eval(input())
b='a'
for i in a:
    b += str(i)
    c=list(b[1:])
    c.sort()
d=[]
for r in c:
    if not r in d:
        e=c.count(r)
        print("%s,%d"%(r,e))
        d.append(r)


