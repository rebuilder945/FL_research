a=list(eval(input()))
n,m=eval(input())
c=len(a)
if n<0:
    if n not in range(-c,0,1):
        print('error')
    else:
        b=a[n]
        for i in range(m):
            a.append(b)
        print(a)
else:
    if n not in range(0,c,1):
        print('error')
    else:
        b=a[n]
        for x in range(m):
            a.append(b)
        print(a)

