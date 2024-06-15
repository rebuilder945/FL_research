a=eval(input())
b=[0,1]
for x in a:
    for i in range(2,x):
        if x%i==0:
            b.append(x)
        else:
            continue
c=list(set(a).difference(set(b)))
print(c)
