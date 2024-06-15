a=eval(input())
a.sort(reverse=True)
b=[str(x) for x in a]
c=''.join(b)
d=int(c)
print(d)
