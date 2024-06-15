n=eval(input())
m=eval(input())
if n+3==m and 0<=n<=6:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and a!=c and b!=c:
                    number=a*100+b*10+c
                    if number>99:
                        print(number,end='')
else:
    print("illegal input")
