a=list(map(int,input().split(',')))
n,m=eval(input())
d=[]
if n<=len(a):
    for x in range(m):
        d.append(a[n])
    a=a+d
    print(a)
else:
    print('error')

'''a=list(map(str,input().split(',')))
n,m=map(int,input().split(','))
if n<=len(a):
    b=a[n]
    c=b*m
    a=a+list(c)
    d= '[' + ','.join(a) + ']'
    print(d)
else:
    print('error')'''
