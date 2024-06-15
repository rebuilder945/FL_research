n,m=map(int,input().split())
if n<m and 0<=n<=9 and 0<m<=9:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and a!=c and b!=c:
                    number=a*100+b*10+c
                    if number>99:
                        print(number,end=' ')
else:
    print("illegal input")
