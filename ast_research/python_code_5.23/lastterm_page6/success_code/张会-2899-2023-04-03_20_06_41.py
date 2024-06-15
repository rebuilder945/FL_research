n,m = map(int,input().split())
if 0<= n < m <11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b != c and c != a:
                    n = 100*a+10*b+c
                    if n>99:
                        print(n,end=" ")
else:
    print('illegal input')
