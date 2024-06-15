n,m=map(int,input().split(' '))
if m-n>=3 and m<11 and n>=0:
    for a in range (n,m):
        for b in range (n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    s=a*100+b*10+c
                    if s>99:
                        print(s,end=' ')
else:
    print('illegal input')

