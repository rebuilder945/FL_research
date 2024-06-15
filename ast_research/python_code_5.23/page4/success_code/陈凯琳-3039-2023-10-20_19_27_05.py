lit=eval(input())
Imax=int(max(lit))
Imin=int(min(lit))
Nmax=lit.count(Imax)
Nmin=lit.count(Imin)
a=0
b=0
if Imax != Imin:
    while a<Nmax :
        lit.remove(Imax)
        a+=1
    while b<Nmin:
        lit.remove(Imin)
        b+=1
    print(lit)
elif Imax==Imin:
    print([])




