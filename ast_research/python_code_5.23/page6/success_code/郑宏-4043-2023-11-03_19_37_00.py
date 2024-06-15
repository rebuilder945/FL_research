from copy import copy
a=eval(input())
b=(''.join(a))
print(b)
c=[]
for i in range(len(b)):
    c.append(b[i])
e=c.copy()
c=list(set(c))
c.sort()
print(c)
for i in c:
    print('%s,%d'%(i,e.count(i)))


