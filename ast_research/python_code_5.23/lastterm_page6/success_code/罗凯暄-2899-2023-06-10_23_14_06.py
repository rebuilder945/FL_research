n, m = map(int, input().split())
if n >= m or n < 0 or m > 100:
    print("illegal input")
else:
    for i in range(n, m):
        for j in range(n, m):
            for k in range(n, m):
                if i != j and i != k and j != k:
                    print(i*100+j*10+k, end=' ')

