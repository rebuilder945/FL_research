n, m = map(int, input().split())

if n >= m or n < 0 or m > 100:
    print("illegal input")
else:
    result = []
    for i in range(n, m):
        for j in range(n, m):
            for k in range(n, m):
                if i != j and j != k and i != k:
                    num = i * 100 + j * 10 + k
                    if num >= 100 and num < 1000:
                        result.append(num)
    if len(result) == 0:
        print("illegal input")
    else:
        print(*result)
