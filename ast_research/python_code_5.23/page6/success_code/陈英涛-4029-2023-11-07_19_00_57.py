n,m = map(int,input().split(" "))
if n < m and m < 11:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and a != c and b != c:
                    d = a*100 + b*10 + c
                    print(d, end=" ")
else:
    print("illegal input")
