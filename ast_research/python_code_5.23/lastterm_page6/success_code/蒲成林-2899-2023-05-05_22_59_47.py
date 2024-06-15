n, m = map(int, input().split())

if n >= m:
    print("illegal input")
else:
    found = False
    for i in range(100, 1000):
        hundreds = i // 100
        tens = (i // 10) % 10
        ones = i % 10
        if hundreds != tens and hundreds != ones and tens != ones and hundreds >= n and tens >= n and ones >= n and hundreds < m and tens < m and ones < m:
            print(i, end=' ')
            found = True
    if not found:
        print("illegal input")
