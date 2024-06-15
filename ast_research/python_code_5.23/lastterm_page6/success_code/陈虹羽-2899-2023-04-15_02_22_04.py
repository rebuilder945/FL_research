a=input().split(' ')
d=int(a[0])
e=int(a[-1])
if d>=e or d<0 or d==e or e-d<=2 or e>=10 or d>=10:
    print('illegal input')
else:
    for a in range(d,e):
        for b in range(d,e):
           for c in range(d,e):
                if a!=b and b!=c and c!=a:
                    N=a*100+b*10+c
                    if N>99:
                        print(N,end=" ")



