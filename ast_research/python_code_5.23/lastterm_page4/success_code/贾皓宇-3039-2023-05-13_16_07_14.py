a=eval(input())
imax=max(a)
imin=min(a)
for x in range(a.count(imax)):
    a.remove(imax)
for y in range(a.count(imin)):
    a.remove(imin)
print(a)
