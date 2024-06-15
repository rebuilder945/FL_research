a=eval(input())
c=''.join(a)
d=sorted(list(c))
e=[]
for x in d:
    if x not in e:
        e.append(x)
        b=c.count(x)
        print(x+','+b)
