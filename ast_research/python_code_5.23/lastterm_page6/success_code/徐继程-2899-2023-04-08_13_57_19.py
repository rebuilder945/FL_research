n,m=map(int,input().split())

coun=0
if type(n)!=type(0) or type(m)!=type(0):
    print('illegal input')
if n>=m:
    print('illegal input')
elif n<m:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    if a!=0 and a*100+b*10+c in range(100,1000):
                        print(a*100+b*10+c,end=' ')
                        coun+=1
    if coun==0:
        print('illegal input')

