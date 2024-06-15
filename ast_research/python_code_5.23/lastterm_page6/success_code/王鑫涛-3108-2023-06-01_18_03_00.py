a=eval(input())
b='a'
for i in a:
    b += str(i)
    c=b[1:]
    print(i)
d=[]
for r in c:
    if not r in d:
        e=c.count(r)
        print("%s,%d"%(r,e))
        d.append(r)


