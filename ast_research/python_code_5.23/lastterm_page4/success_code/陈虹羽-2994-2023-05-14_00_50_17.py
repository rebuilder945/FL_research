a=list(eval(input()))
n,m=eval(input())
c=len(a)
if n<0:
    if n not in range(-c,0,1):
        print('error')
    else:
        for i in range(m):
            a.append(a[n])
        print(a)
else:
    if n not in range(0,c,1):
        print('error')
    else:
        for x in range(m):
            a.append(a[n])
        print(a)

