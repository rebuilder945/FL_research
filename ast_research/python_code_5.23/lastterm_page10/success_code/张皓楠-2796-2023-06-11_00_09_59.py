m=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
n=list('abcdefghijklmnopqrstuvwxyz')
a=list(input())
b=[]
for i in a:
    if i in m:
        x=m.index(i)
        t=m[25-x]

    elif i in n:
        x=n.index(i)
        t=n[25-x]
    else:
        t=i
    b.append(t)
print(''.join(a))
print(''.join(b))






