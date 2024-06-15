a=eval(input())
b=[]
d=[]
for i in range(len(a)):
    c=a[i]
    if c == 1:
        d=c
    elif c == 0:
        d=c
    elif c == 2:
        b.append(c)
    else:
        for x in range(2,c):
            if c % x == 0:
                break
        else:
            b.append(c)
print(b)
