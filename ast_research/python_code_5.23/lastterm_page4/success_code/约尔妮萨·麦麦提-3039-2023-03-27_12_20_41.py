yy=eval(input())
lmax=int(max(yy))
lmin=int(min(yy))
Nmax=yy.count(lmax)
Nmin=yy.count(lmin)
a=0
b=0
if lmax!=lmin:
    while a<Nmax:
        yy.remove(lmax)
        a+=1
    while b<Nmin:
        yy.remove(lmin)
        b+=1
    print(yy)
elif lmax==lmin:
    yy.clear()
    print(yy)
