list=eval(input())
a=list.sort(reverse=True)
b=[str(x) for x in a]
c=''.join(b)
d=int(c)
print(c)
