a=eval(input())
c=''.join(a)
d=sorted(list(c))
for x in d:
    b=c.count(x)
    print(x,b)
