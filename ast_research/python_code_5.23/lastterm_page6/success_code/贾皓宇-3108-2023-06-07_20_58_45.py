a=eval(input())
b=list(''.join(x for x in a))
c=list(set(b))
c.sort()
for x in c:
    s=b.count(x)
    print('%s,%d'%(x,s))

