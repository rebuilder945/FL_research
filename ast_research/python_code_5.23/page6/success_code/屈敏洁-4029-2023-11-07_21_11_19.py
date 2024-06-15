n,m = map(int,input().split())
if n<m and m-n>3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b != c and a != c:
                    n = a*100+b*10+c
                    print(n,end=' ')
else:
    print("illegal input")    
    
