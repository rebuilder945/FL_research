n,m=eval(input())
if n+2>=m:
    print("illegal input")
for a in range(n,m):
    for b in range(n,m):
        for c in range(n,m):
            if a!=b and b!=c and a!=c:
                N=a*100+b*10+c
                if N>99:
                    print(N,end=" ")
