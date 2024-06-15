a=eval(input())
b=set(a)
c=list(b)
c.sort()
del c[0]
del c[-1]
print(c)
