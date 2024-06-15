n, m, l = map(int, input().split(','))
result = [n + i * l for i in range(m)]
print(result)
