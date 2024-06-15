n, m = map(int, input().split())

if n >= m or n < 100 or m > 1000:
    print("illegal input")
else:
    for i in range(n, m):
        if len(set(str(i))) == 3:
            print(i, end=" ")
