lt=eval(input())
l=len(lt)
s=0
ii=list()
for i in range(l):
    a=max(lt)
    ii.append(a)
    lt.remove(a)
# float([1,2])
#TypeError: float() argument must be a string or a number, not 'list'
for y in range(l):
    z=ii[-1]
    s=s+z*10**y
    ii.remove(z)
print(s)

