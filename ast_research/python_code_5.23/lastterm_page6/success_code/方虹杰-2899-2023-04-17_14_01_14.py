n,m=map(int,input().split())
if n>=m or m>=10 or n<0 or m-n<3:
    print("illgeal input")
else:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    N=a*100+b*10+c
                    if n>99:
                        print(N,end='')
                        
