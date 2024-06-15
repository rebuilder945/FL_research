a=eval(input())
b=list(''.join(x for x in a))
c=set(b)
for x in c:
    s=b.count(x)
    print(x,s)
