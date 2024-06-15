a=eval(input())
b="".join(a)
c=list(b)
c.sort()
for x in a:
    print(x,a.count(x))
