a1 = eval(input())
b1 = "".join("%s"%i for i in a1)
c1 = list(b1)
n1=0
d1 = []
for i in c1:
    n1 = c1.count(i)
    e1 = "%s,%d"%(i,n1)
    d1.append(e1)
f1=set(d1)
g1=list(f1)
g1.sort()
print("\n".join("%s"%t1 for t1 in g1))
