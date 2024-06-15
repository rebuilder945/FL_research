a=eval(input())
a=''.join(a)
b=set(a)
b=list(b)
b.sort()
for i in b:
    print('%s,%d'%(i,a.count(i)))
