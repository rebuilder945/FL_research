a=input()
b='a'
for i in a:
    b += i
    c=list(b[1:])
    c.sort()

d=[]
for r in c:
    if not i in d:
        e=i.count(c)
        print(i,e)
        d.append(i)

